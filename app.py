from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bots import get_bot_response
from memory import session_memory
from utils import translate_input, translate_output, log_event
import datetime
from pydantic import BaseModel, constr
import re
from collections import Counter
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    session_id: constr(min_length=1)
    message: constr(min_length=1, max_length=1000)
    language: str = "en"
    bot_name: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat")
async def chat(data: ChatRequest):
    session_id = data.session_id
    user_input = sanitize(data.message)
    language = data.language
    bot_name = data.bot_name

    log_event("query", f"[{session_id}] to {bot_name}: {user_input}")
    log_event("bot_usage", bot_name)

    if session_id not in session_memory:
        session_memory[session_id] = []

    translated_input = translate_input(user_input, language) if language != "en" else user_input
    session_memory[session_id].append(("user", translated_input))

    bot_reply = get_bot_response(bot_name, translated_input)
    session_memory[session_id].append((bot_name, bot_reply))

    translated_reply = translate_output(bot_reply, language) if language != "en" else bot_reply

    return {
        "reply": translated_reply,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "history": session_memory[session_id],
    }

@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    log_file = "logs/backend.log"
    if not os.path.exists(log_file):
        return HTMLResponse("<h2>No logs found yet.</h2>")

    bot_usage = []
    queries = []
    translation_errors = []

    with open(log_file, "r") as f:
        for line in f:
            if "BOT_USAGE" in line:
                bot = line.strip().split(":")[-1].strip()
                bot_usage.append(bot)
            elif "QUERY" in line:
                msg = line.strip().split("to")[-1].strip()
                queries.append(msg)
            elif "TRANSLATION_ERROR" in line:
                lang_msg = line.strip().split(":")[-1].strip()
                translation_errors.append(lang_msg)

    usage_stats = Counter(bot_usage).most_common()
    query_stats = Counter(queries).most_common(5)
    failed_translations = Counter(translation_errors).most_common(5)

    return templates.TemplateResponse("admin.html", {
        "request": request,
        "usage_stats": usage_stats,
        "query_stats": query_stats,
        "translation_errors": failed_translations
    })

def sanitize(text):
    text = text.strip()
    text = re.sub(r"[<>]", "", text)  # Prevent HTML injection
    return text

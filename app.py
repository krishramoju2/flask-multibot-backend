from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bots import get_bot_response
from memory import session_memory
from utils import translate_input, translate_output
import datetime

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


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/chat")
async def chat(data: dict):
    session_id = data.get("session_id")
    user_input = data.get("message")
    language = data.get("language", "en")
    bot_name = data.get("bot_name")

    if not all([session_id, user_input, bot_name]):
        return JSONResponse(status_code=400, content={"error": "Missing fields"})

    if session_id not in session_memory:
        session_memory[session_id] = []

    translated_input = translate_input(user_input, language)
    session_memory[session_id].append(("user", translated_input))

    bot_reply = get_bot_response(bot_name, translated_input)
    session_memory[session_id].append((bot_name, bot_reply))

    translated_reply = translate_output(bot_reply, language)

    return {
        "reply": translated_reply,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "history": session_memory[session_id]
    }

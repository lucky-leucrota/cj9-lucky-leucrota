from fastapi import APIRouter, WebSocket, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import random
import string

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")

alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)

def caesar(text, step, alphabets):
    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)

@router.get("/")
async def index(request: Request):
    """Index Route"""
    return templates.TemplateResponse("index.html", {"request": request})

websocket_list = []

websocket_list = []
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    if websocket not in websocket_list:
        websocket_list.append(websocket)

    while True:
        content = await websocket.receive_text()
        
        for ws in websocket_list:
            if ws != websocket:
                await ws.send_text(caesar(content, random.randint(1, 10), alphabets))

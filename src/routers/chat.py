from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates

from .utillity import ConnectionManager

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")

manager = ConnectionManager()


@router.get("/")
async def index(request: Request):
    """Index Route"""
    return templates.TemplateResponse("index.html", {"request": request})


@router.websocket("/ws/{client_name}")
async def websocket_endpoint(websocket: WebSocket, client_name: str):
    """Websocket Route"""
    await manager.connect(client_name, websocket)

    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(client_name, websocket, message)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(client_name, websocket, disconnected=True)

from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates

from .utillity import ConnectionManager

router = APIRouter()

templates = Jinja2Templates(directory="src/templates")

manager = ConnectionManager()


@router.get("/chat")
async def index(request: Request):
    """Root page of the chat application."""
    return templates.TemplateResponse("chat.html", {"request": request})


@router.websocket("/ws/{client_name}")
async def websocket_endpoint(websocket: WebSocket, client_name: str):
    """Websocket endpoint for the chat application."""
    await manager.connect(client_name, websocket)

    try:
        while True:
            message = await websocket.receive_text()
            await manager.broadcast(
                client_name=client_name,
                websocket=websocket,
                message=message,
                disconnected=False,
            )

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(client_name, websocket, disconnected=True)

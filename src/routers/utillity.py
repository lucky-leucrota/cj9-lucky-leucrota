from fastapi import WebSocket
from typing import List

import random
import string

def caesar(text, step, alphabets):
    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)

alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)

class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: List[WebSocket] = []

    async def connect(self, client_name: str, websocket: WebSocket) -> None:
        await websocket.accept()
        self.active_connections.append(websocket)

        for connection in self.active_connections:
            if connection != websocket:
                await connection.send_text(f"{client_name} join the chat room.")

    def disconnect(self, websocket: WebSocket) -> None:
        self.active_connections.remove(websocket)

    async def broadcast(
        self,
        client_name: str,
        websocket: WebSocket,
        message: str = "",
        disconnected: bool = False,
    ) -> None:
        if disconnected:
            for connection in self.active_connections:
                if connection != websocket:
                    await connection.send_text(f"{client_name} left the chat room.")

        else:
            for connection in self.active_connections:
                if connection != websocket:
                    await connection.send_text(f"{client_name}: {caesar(message, random.randint(1, 100), alphabets)}")
                else:
                    await connection.send_text(f"You: {message}")
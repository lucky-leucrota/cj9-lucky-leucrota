import random
import string
from typing import List

from fastapi import WebSocket


def caesar(text, step, alphabets):
    """Caesar cipher"""
    def shift(alphabet):
        """Shift alphabet"""
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_aphabets = "".join(alphabets)
    joined_shifted_alphabets = "".join(shifted_alphabets)
    table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
    return text.translate(table)


alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)


class ConnectionManager:
    """Connection Manager"""

    def __init__(self) -> None:
        """Initialize Connection Manager"""
        self.active_connections: List[WebSocket] = []

    async def connect(self, client_name: str, websocket: WebSocket) -> None:
        """Connect to the chat room"""
        await websocket.accept()
        self.active_connections.append(websocket)

        for connection in self.active_connections:
            if connection != websocket:
                await connection.send_text(f"{client_name} join the chat room.")

    def disconnect(self, websocket: WebSocket) -> None:
        """Disconnect from the chat room"""
        self.active_connections.remove(websocket)

    async def broadcast(
        self,
        client_name: str,
        websocket: WebSocket,
        message: str = "",
        disconnected: bool = False,
    ) -> None:
        """Broadcast message to all active connections"""
        if disconnected:
            for connection in self.active_connections:
                if connection != websocket:
                    await connection.send_text(f"{client_name} left the chat room.")

        else:
            for connection in self.active_connections:
                if connection != websocket:
                    En_message = caesar(message, random.randint(1, 25), alphabets)
                    print(message)
                    await connection.send_text(f"{client_name}: {En_message}")
                else:
                    await connection.send_text(f"You: {message}")

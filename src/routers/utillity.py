import logging
import os
import random
from typing import Callable, Dict, List
from .algorithms import *

from fastapi import WebSocket


# configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
    style="%",
    filemode="a",
    filename=os.path.abspath("src/logs/chat.log"),
)


class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: List[WebSocket] = []
        self.algorithm: Dict[str, Dict[str, Callable]] = {
            "monoalpabetic": {
                "encrypt": monoalpabetic_encrypt,
                "decrypt": monoalpabetic_decrypt,
            },
            "vigenere": {
                "encrypt": vigenere_encrypt,
                "decrypt": vigenere_decrypt,
            },
            "caeser": {
                "encrypt": caeser_encrypt,
                "decrypt": caeser_decrypt,
            },
            "tansposition": {
                "encrypt": tansposition_encrypt,
                "decrypt": tansposition_decrypt,
            },
        }
        self.all_algorithm_names: List[str] = list(self.algorithm.keys())

    async def connect(self, client_name: str, websocket: WebSocket) -> None:
        """Add a new connection to the list of active connections."""
        await websocket.accept()
        self.active_connections.append(websocket)

        for connection in self.active_connections:
            if connection != websocket:
                await connection.send_text(f"{client_name} joined the chat room.")

    def disconnect(self, websocket: WebSocket) -> None:
        """Remove a connection from the list of active connections."""
        self.active_connections.remove(websocket)

    async def broadcast(
        self,
        client_name: str,
        websocket: WebSocket,
        message: str = "",
        disconnected: bool = False,
    ) -> None:
        """Broadcast a message to all active connections."""
        if disconnected:
            for connection in self.active_connections:
                if connection != websocket:
                    await connection.send_text(f"{client_name} left the chat room.")

        else:
            flag: int = random.randint(0, 100)
            algorithm_name: str = random.choice(self.all_algorithm_names)

            try:
                message_encrypt: str = self.algorithm[algorithm_name]["encrypt"](
                    message
                )
                message_decrypt: str = self.algorithm[algorithm_name]["decrypt"](
                    message_encrypt
                )
            except Exception as e:
                flag: int = 100
                message_encrypt: str = message
                message_decrypt: str = message
                logging.error(f"in encryption/decryption: {e}")

            for connection in self.active_connections:
                if connection != websocket:
                    if flag < 20:
                        print(f"{client_name}: {message_encrypt} [algorithm = '{algorithm_name} cipher']")
                        await connection.send_text(
                            f"{client_name}: {message_encrypt} [algorithm = '{algorithm_name} cipher']"
                        )
                    else:
                        await connection.send_text(f"{client_name}: {message_decrypt}")
                else:
                    await connection.send_text(f"You: {message_decrypt}")

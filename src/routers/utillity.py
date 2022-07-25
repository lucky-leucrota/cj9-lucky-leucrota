from typing import Callable, Dict, List
from fastapi import WebSocket
from .algorithem import *

import random
# import string
#
# def caesar(text, step, alphabets):
#     """Caesar cipher"""
#     def shift(alphabet):
#         """Shift alphabet"""
#         return alphabet[step:] + alphabet[:step]

#     shifted_alphabets = tuple(map(shift, alphabets))
#     joined_aphabets = "".join(alphabets)
#     joined_shifted_alphabets = "".join(shifted_alphabets)
#     table = str.maketrans(joined_aphabets, joined_shifted_alphabets)
#     return text.translate(table)


# alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)


class ConnectionManager:
    """The Websocket Manager"""

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
        }

    async def connect(self, client_name: str, websocket: WebSocket) -> None:
        """Add a new connection to the list of active connections."""
        await websocket.accept()
        self.active_connections.append(websocket)

        for connection in self.active_connections:
            if connection != websocket:
                await connection.send_text(f"{client_name} join the chat room.")

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
            flag = random.randint(0, 100)
            algorithm_name = random.choice(list(self.algorithm.keys()))

            try:
                message_encrypt = self.algorithm[algorithm_name]["encrypt"](message)
                message_decrypt = self.algorithm[algorithm_name]["decrypt"](
                    message_encrypt
                )
            except Exception as e:
                # TODO: add logging
                print(e)
                message_encrypt = message
                message_decrypt = message
                flag = 100

            for connection in self.active_connections:
                if connection != websocket:
                    if flag < 25:
                        await connection.send_text(
                            f"{client_name}: {message_encrypt}, algorithm: {algorithm_name} cipher"
                        )
                    else:
                        await connection.send_text(f"{client_name}: {message_decrypt}")
                else:
                    await connection.send_text(f"You: {message_decrypt}")

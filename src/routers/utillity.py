from importlib.util import set_loader
import logging
import os
import random
from typing import Callable, Dict, List

from fastapi import WebSocket

from .algorithem import *
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
                "key": "luckyleucrota"
            },
            "one-time-pad": {
                "encrypt": one_time_pad_encrypt,
                "decrypt": one_time_pad_decrypt,
                "key": bytes("luckyleucrota", "utf-8")
            },
            "Permutation": {
                "encrypt": permutation_cipher_encrypt,
                "decrypt": permutation_cipher_decrypt,
                "key": permutation_cipher_gen_key()
            }
        }
        self.all_algorithm_names: List[str] = list(self.algorithm.keys())

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
            flag: int = random.randint(0, 100)
            algorithm_name: str = random.choice(self.all_algorithm_names)
            try:
                if algorithm_name == "one-time-pad" or algorithm_name == "Permutation":
                    message_encrypt = str(self.algorithm[algorithm_name]["encrypt"](
                        bytes(message, "utf-8"),
                        self.algorithm[algorithm_name]["key"]
                    ))
                    message_decrypt = str(self.algorithm[algorithm_name]["decrypt"](
                        bytes(str(message_encrypt), "utf-8"),
                        self.algorithm[algorithm_name]["key"]
                    ))
                else:
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
                    if flag < 45:
                        try:
                            key = self.algorithm[algorithm_name]["key"]
                        except:
                            key = "No Keys, in this cipher"
                        await connection.send_text(
                            f"{client_name}: {message_encrypt}, algorithm: {algorithm_name} cipher, Key: {key}"
                        )
                    else:
                        await connection.send_text(f"{client_name}: {message_decrypt}")
                else:
                    await connection.send_text(f"You: {message_decrypt}")

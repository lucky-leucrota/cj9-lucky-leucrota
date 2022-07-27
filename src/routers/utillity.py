from importlib.util import set_loader
import logging
import os
import random
from typing import Callable, Dict, List

from src.encrypt.encryption_facade import CipherFacade

from fastapi import WebSocket

# from .algorithem import *
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

        # self.algorithm: Dict[str, Dict[str, Callable]] = {
        #     "monoalpabetic": {
        #         "encrypt": monoalpabetic_encrypt,
        #         "decrypt": monoalpabetic_decrypt,
        #     },
        #     "vigenere": {
        #         "encrypt": vigenere_encrypt,
        #         "decrypt": vigenere_decrypt,
        #         "key": "luckyleucrota"
        #     },
        #     "one-time-pad": {
        #         "encrypt": one_time_pad_encrypt,
        #         "decrypt": one_time_pad_decrypt,
        #         "key": bytes("luckyleucrota", "utf-8")
        #     },
        #     "Permutation": {
        #         "encrypt": permutation_cipher_encrypt,
        #         "decrypt": permutation_cipher_decrypt,
        #         "key": permutation_cipher_gen_key()
        #     }
        # }
        # self.all_algorithm_names: List[str] = list(self.algorithm.keys())

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

    def _generate_random_encryptor(self, message_len) -> CipherFacade:
        algorithm_name: str = random.choice(CipherFacade.encryption_schemes.keys())
        config = {"scheme": algorithm_name}

        if config["scheme"] == "OneTimePad":
            config["key_args"] = {"length": len(message)}
        elif config["scheme"] in ["TranspositionCipher", "VigenereCipher"]:
            config["key_args"] = {"length": 6}

        return CipherFacade(config)

    def _generate_encrypted_message_payload(
        self, encryptor: CipherFacade, message: str
    ) -> Dict[str, str]:
        payload = {}
        try:
            payload["encryption_scheme"] = encryptor.config["scheme"]
            payload["encrypted_message"] = encryptor.encrypt(message)
            payload["decrypted_message"] = encryptor.decrypt(
                payload["encrypted_message"]
            )
            payload["key"] = cipher_facade.get_key()

        except Exception as e:
            payload = {"message": message}
            logging.error(f"in encryption/decryption: {e}")

    def generate_message(self, client_name: str, message: str) -> str:
        encryptor = self._generate_random_encryptor(len(message))
        payload = self._generate_encrypted_message_payload(encryptor, message)

        flag: int = random.randint(0, 100)
        if (
            flag < 20 and "encryption_scheme" in payload
        ):  # 20% of the messages are encrypted, if we placed more it will be annoying.
            key = payload["key"]
            if key == None:
                key = "No Keys, in this cipher"

            return f"{client_name}: {payload['encrypted_message']}, algorithm: {payload['encryption_scheme']} cipher, Key: {payload['key']}"

        else:
            return f"{client_name}: {payload['message']}"

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
            for connection in self.active_connections:
                if connection != websocket:
                    await connection.send_text(
                        self.generate_message(client_name, message)
                    )
                else:
                    await connection.send_text(f"You: {message}")

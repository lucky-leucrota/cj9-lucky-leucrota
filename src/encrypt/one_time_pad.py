import secrets
import codecs


class OneTimePadCipher:
    def encrypt(self, plain_text: bytes, key: bytes) -> bytes:
        return bytes([p ^ k for p, k in zip(plain_text, key)])

    def decrypt(self, cipher_text: bytes, key: bytes) -> bytes:
        return self.encrypt(cipher_text, key)

    def genkey(self, length: int) -> bytes:
        return secrets.token_bytes(length)


class OneTimePadEncoder:
    def encode_plaintext(self, plain_text: str) -> bytes:
        return bytes(plain_text, "utf-8")

    def decode_encrypted_message(self, encrypted_message: bytes) -> str:
        return encrypted_message.hex()

    def encode_encrypted_message(self, encrypted_message: str) -> bytes:
        return codecs.decode(encrypted_message, "hex")

    def decode_decrypted_message(self, decrypted_message: bytes) -> str:
        return decrypted_message.hex()

    def decode_key(self, key: bytes) -> str:
        return key.hex()

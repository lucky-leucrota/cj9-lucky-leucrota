import random
from typing import List


class SubsitutionCipher:
    def encrypt(self, plain_text: bytes, key: List[int]) -> bytes:
        cipher_text = [c for c in plain_text]
        for i in range(len(plain_text)):
            cipher_text[i] = key[plain_text[i]]
        return bytes(cipher_text)

    def decrypt(self, cipher_text: bytes, key: List[int]) -> bytes:
        return self.encrypt(cipher_text, self.inverse_permutation(key))

    def inverse_permutation(self, key: List[int]) -> List[int]:
        inverse_permutation = [0] * len(key)
        for i in range(len(key)):
            inverse_permutation[key[i]] = i
        return inverse_permutation

    def genkey(self) -> List[int]:
        key = [i for i in range(256)]
        random.shuffle(key)
        return key


class SubsitutionCipherEncoder:
    def encode_plaintext(self, plain_text: str) -> bytes:
        return bytes(plain_text, "utf-8")

    def decode_encrypted_message(self, encrypted_message: bytes) -> str:
        return str(encrypted_message, "cp437")

    def encode_encrypted_message(self, encrypted_message: str) -> bytes:
        return bytes(encrypted_message, "cp437")

    def decode_decrypted_message(self, decrypted_message: bytes) -> str:
        return str(decrypted_message, "utf-8")

    def decode_key(self, key: bytes) -> str:
        return key.hex()

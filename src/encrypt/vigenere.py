import secrets
import string
from typing import List


class VigenereCipher:
    def encrypt(self, plain_text: str, key: str) -> str:
        key = (key * (len(plain_text) // len(key))) + key[: len(plain_text) % len(key)]
        letters = (
            string.ascii_lowercase
            + string.ascii_lowercase
            + string.ascii_uppercase
            + string.ascii_uppercase
        )
        ans = ""
        for i in range(len(plain_text)):
            if plain_text[i] in letters and key[i] in letters:
                if plain_text[i].isupper():
                    ans += letters[
                        (letters.index(plain_text[i]) + letters.index(key[i])) % 26
                    ].upper()
                else:
                    ans += letters[
                        (letters.index(plain_text[i]) + letters.index(key[i])) % 26
                    ].lower()
            else:
                ans += plain_text[i]

        return ans

    def decrypt(self, cipher_text: str, key: str) -> str:
        key = (key * (len(cipher_text) // len(key))) + key[
            : len(cipher_text) % len(key)
        ]
        letters = (
            string.ascii_lowercase
            + string.ascii_lowercase
            + string.ascii_uppercase
            + string.ascii_uppercase
        )
        ans = ""
        for i in range(len(cipher_text)):
            if cipher_text[i] in letters and key[i] in letters:
                if cipher_text[i].isupper():
                    ans += letters[
                        (letters.index(cipher_text[i]) - letters.index(key[i])) % 26
                    ].upper()
                else:
                    ans += letters[
                        (letters.index(cipher_text[i]) - letters.index(key[i])) % 26
                    ].lower()
            else:
                ans += cipher_text[i]

        return ans

    def genkey(self, length: int = 100) -> str:
        return str([secrets.choice(string.ascii_letters) for i in range(length)])


class VigenereCipherEncoder:
    def encode_plaintext(self, plain_text: str) -> str:
        return str(bytes(plain_text, "utf-8"), "cp437")

    def decode_encrypted_message(self, encrypted_message: str) -> str:
        return encrypted_message

    def encode_encrypted_message(self, encrypted_message: str) -> str:
        return encrypted_message

    def decode_decrypted_message(self, decrypted_message: str) -> str:
        return str(bytes(decrypted_message, "cp437"), "utf-8")

    def decode_key(self, key: int) -> str:
        return str(key)

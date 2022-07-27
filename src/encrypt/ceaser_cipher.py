import string
import random


class CeaserCipher:
    def encrypt(self, plain_text: str, key: int) -> str:
        letters = (
            string.ascii_lowercase
            + string.ascii_lowercase
            + string.ascii_uppercase
            + string.ascii_uppercase
        )

        cipher_text = ""
        for i in plain_text:
            if i in letters:
                cipher_text += letters[(letters.index(i) + key)]
            else:
                cipher_text += i

        return cipher_text

    def decrypt(self, cipher_text: str, key: int) -> str:
        letters = (
            string.ascii_lowercase
            + string.ascii_lowercase
            + string.ascii_uppercase
            + string.ascii_uppercase
        )

        decrypted_text = ""
        for i in cipher_text:
            if i in letters:
                decrypted_text += letters[(letters.rindex(i) - key)]
            else:
                decrypted_text += i

        return decrypted_text

    def genkey(self) -> int:
        return random.randint(1, 26)


class CeaserCipherEncoder:
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

import math
import secrets
import string


class TranspositionCipher:
    def encrypt(self, plain_text: str, key: str):
        plaintext_length = float(len(plain_text))
        plaintext_list = list(plain_text)
        key_list = list(key)
        sorted_keylist = sorted(list(key))

        column_count = len(key)
        row_count = int(math.ceil(plaintext_length / column_count))

        fill_null = int((row_count * column_count) - plaintext_length)
        plaintext_list.extend("_" * fill_null)

        matrix = [
            plaintext_list[i : i + column_count]
            for i in range(0, len(plaintext_list), column_count)
        ]

        cipher_text = ""

        key_idx = 0
        for _ in range(column_count):
            curr_idx = key_list.index(sorted_keylist[key_idx])
            key_list[curr_idx] = "_"
            cipher_text += "".join([row[curr_idx] for row in matrix])
            key_idx += 1

        return cipher_text

    def decrypt(self, cipher_text: str, key: str) -> str:
        ciphertext_length = float(len(cipher_text))
        column_count = len(key)
        row_count = int(math.ceil(ciphertext_length / column_count))

        key_list = list(key)
        sorted_keylist = sorted(list(key))
        matrix = [[None] * column_count for i in range(row_count)]

        for i in range(column_count):
            curr_idx = key_list.index(sorted_keylist[i])
            key_list[curr_idx] = "_"

            for j in range(row_count):
                matrix[j][curr_idx] = cipher_text[i * row_count + j]

        decrypted_message = ""
        try:
            decrypted_message = "".join(sum(matrix, []))
        except TypeError:
            raise TypeError("This program cannot", "handle repeating words.")

        null_count = decrypted_message.count("_")

        if null_count > 0:
            return decrypted_message[:-null_count]

        return decrypted_message

    def genkey(self, length: int = 100) -> str:
        return str([secrets.choice(string.ascii_letters) for i in range(length)])


class TranspositionCipherEncoder:
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

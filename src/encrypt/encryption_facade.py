from src.encrypt.one_time_pad import OneTimePadCipher, OneTimePadEncoder
from src.encrypt.substitution_cipher import SubsitutionCipher, SubsitutionCipherEncoder
from src.encrypt.ceaser_cipher import CeaserCipher, CeaserCipherEncoder
from src.encrypt.transposition_cipher import (
    TranspositionCipher,
    TranspositionCipherEncoder,
)
from src.encrypt.vigenere import VigenereCipher, VigenereCipherEncoder

from typing import Dict


class CipherFacade:

    encryption_schemes = {
        "OneTimePad": OneTimePadCipher,
        "SubstitutionCipher": SubsitutionCipher,
        "CeaserCipher": CeaserCipher,
        "TranspositionCipher": TranspositionCipher,
        "VigenereCipher": VigenereCipher,
    }

    encoders = {
        "OneTimePad": OneTimePadEncoder,
        "SubstitutionCipher": SubsitutionCipherEncoder,
        "CeaserCipher": CeaserCipherEncoder,
        "TranspositionCipher": TranspositionCipherEncoder,
        "VigenereCipher": VigenereCipherEncoder,
    }

    def __init__(self, config: Dict[str, object]) -> None:

        self.cipher = CipherFacade.encryption_schemes[config["scheme"]]()
        self.encoder = CipherFacade.encoders[config["scheme"]]()

        if "key" in config:
            self.key = config["key"]
        elif "key_args" in config:
            self.key = self.cipher.genkey(**config["key_args"])
        else:
            self.key = self.cipher.genkey()

        self.config = config

    def encrypt(self, plain_text: str) -> str:
        encoded_plaintext = self.encoder.encode_plaintext(plain_text)
        encrypted_text = self.cipher.encrypt(encoded_plaintext, self.key)
        return self.encoder.decode_encrypted_message(encrypted_text)

    def decrypt(self, cipher_text: str) -> str:
        encoded_ciphertext = self.encoder.encode_encrypted_message(cipher_text)
        decrypted_text = self.cipher.decrypt(encoded_ciphertext, self.key)
        return self.encoder.decode_decrypted_message(decrypted_text)

    def get_key(self):
        return self.encoder.decode_key(self.key)

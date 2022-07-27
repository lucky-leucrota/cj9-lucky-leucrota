import random
from typing import List
import string
import secrets

import string

PTA = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]|;':,./<>?`~"
CTA = " qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&*()_+-=[]|;':,./<>?`~"


def monoalpabetic_encrypt(pt: str) -> str:
    ans = ""
    for i in pt:
        try:
            ans += CTA[PTA.index(i)]
        except:
            ans += i
    return ans


def monoalpabetic_decrypt(pt: str) -> str:
    ans = ""
    for i in pt:
        try:
            ans += PTA[CTA.index(i)]
        except:
            ans += i
    return ans


def vigenere_encrypt(pt: str, key: str = "luckyleucrota") -> str:
    key = (key * (len(pt) // len(key))) + key[: len(pt) % len(key)]
    letters = (
        string.ascii_lowercase
        + string.ascii_lowercase
        + string.ascii_uppercase
        + string.ascii_uppercase
    )
    ans = ""
    for i in range(len(pt)):
        if pt[i] in letters and key[i] in letters:
            if pt[i].isupper():
                ans += letters[
                    (letters.index(pt[i]) + letters.index(key[i])) % 26
                ].upper()
            else:
                ans += letters[
                    (letters.index(pt[i]) + letters.index(key[i])) % 26
                ].lower()
        else:
            ans += pt[i]

    return ans


def vigenere_decrypt(pt: str, key: str = "luckyleucrota") -> str:
    key = (key * (len(pt) // len(key))) + key[: len(pt) % len(key)]
    letters = (
        string.ascii_lowercase
        + string.ascii_lowercase
        + string.ascii_uppercase
        + string.ascii_uppercase
    )
    ans = ""
    for i in range(len(pt)):
        if pt[i] in letters and key[i] in letters:
            if pt[i].isupper():
                ans += letters[
                    (letters.index(pt[i]) - letters.index(key[i])) % 26
                ].upper()
            else:
                ans += letters[
                    (letters.index(pt[i]) - letters.index(key[i])) % 26
                ].lower()
        else:
            ans += pt[i]

    return ans

def one_time_pad_encrypt(plain_text: bytes, key: bytes) -> bytes:
    return bytes([p ^ k for p, k in zip(plain_text, key)])


def one_time_pad_decrypt(cipher_text: bytes, key: bytes) -> bytes:
    return one_time_pad_encrypt(cipher_text, key)


def one_time_pad_keygen(length: int) -> bytes:
    return secrets.token_bytes(length)


def permutation_cipher_encrypt(plain_text: bytes, key: List[int]) -> bytes:
    cipher_text = [c for c in plain_text]
    for i in range(len(plain_text)):
        cipher_text[i] = key[plain_text[i]]
    return bytes(cipher_text)


def permutation_cipher_decrypt(cipher_text: bytes, key: List[int]) -> bytes:
    return permutation_cipher_encrypt(
        cipher_text, permutation_cipher_inverse_permutation(key)
    )


def permutation_cipher_inverse_permutation(key: List[int]) -> List[int]:
    inverse_permutation = [0] * len(key)
    for i in range(len(key)):
        inverse_permutation[key[i]] = i
    return inverse_permutation


def permutation_cipher_gen_key() -> List[int]:
    key = [i for i in range(256)]
    random.shuffle(key)
    return key
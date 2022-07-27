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

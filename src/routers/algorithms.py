import math
import string


# monoalpabetic cipher
def monoalpabetic_encrypt(pt: str) -> str:
    PTA = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]|;':,./<>?`~"
    CTA = " qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&*()_+-=[]|;':,./<>?`~"

    ans = ""

    for i in pt:
        try:
            ans += CTA[PTA.index(i)]
        except:
            ans += i
    return ans


def monoalpabetic_decrypt(ct: str) -> str:
    PTA = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]|;':,./<>?`~"
    CTA = " qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&*()_+-=[]|;':,./<>?`~"

    ans = ""

    for i in ct:
        try:
            ans += PTA[CTA.index(i)]
        except:
            ans += i
    return ans


# vigenere cipher
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


def vigenere_decrypt(ct: str, key: str = "luckyleucrota") -> str:
    key = (key * (len(ct) // len(key))) + key[: len(ct) % len(key)]

    letters = (
        string.ascii_lowercase
        + string.ascii_lowercase
        + string.ascii_uppercase
        + string.ascii_uppercase
    )

    ans = ""

    for i in range(len(ct)):
        if ct[i] in letters and key[i] in letters:
            if ct[i].isupper():
                ans += letters[
                    (letters.index(ct[i]) - letters.index(key[i])) % 26
                ].upper()
            else:
                ans += letters[
                    (letters.index(ct[i]) - letters.index(key[i])) % 26
                ].lower()
        else:
            ans += ct[i]

    return ans


# caese cipher
def caeser_encrypt(pt: str, key: int = 14) -> str:
    letters = (
        string.ascii_lowercase
        + string.ascii_lowercase
        + string.ascii_uppercase
        + string.ascii_uppercase
    )

    ans = ""

    for i in pt:
        if i in letters:
            ans += letters[(letters.index(i) + key)]
        else:
            ans += i

    return ans.capitalize()


def caeser_decrypt(ct: str, key: int = 14) -> str:
    letters = (
        string.ascii_lowercase
        + string.ascii_lowercase
        + string.ascii_uppercase
        + string.ascii_uppercase
    )

    ans = ""

    for i in ct:
        if i in letters:
            ans += letters[(letters.index(i) - key)]
        else:
            ans += i

    return ans.capitalize()


def tansposition_encrypt(pt: str, key: str = "luckyleucrota") -> str:
    pt_length = float(len(pt))
    pt_list = list(pt)
    key_list = list(key)
    sorted_key_list = sorted(list(key))
    column_count = len(key)
    row_count = int(math.ceil(pt_length / column_count))
    fill_null = int((row_count * column_count) - pt_length)
    pt_list.extend("_" * fill_null)

    matrix = [
        pt_list[i : i + column_count] for i in range(0, len(pt_list), column_count)
    ]

    ans = ""

    key_idx = 0
    for _ in range(column_count):
        curr_idx = key_list.index(sorted_key_list[key_idx])
        key_list[curr_idx] = "_"
        ans += "".join([row[curr_idx] for row in matrix])
        key_idx += 1

    return ans


def tansposition_decrypt(ct: str, key: str = "luckyleucrota") -> str:
    ct_length = float(len(ct))
    column_count = len(key)
    row_count = int(math.ceil(ct_length / column_count))
    key_list = list(key)
    sorted_key_list = sorted(list(key))
    matrix = [[None] * column_count for i in range(row_count)]

    for i in range(column_count):
        curr_idx = key_list.index(sorted_key_list[i])
        key_list[curr_idx] = "_"

        for j in range(row_count):
            matrix[j][curr_idx] = ct[i * row_count + j]  # type: ignore

    ans = ""

    try:
        ans = "".join(sum(matrix, []))  # type: ignore
    except TypeError:
        raise TypeError("can't work with repeating words")

    null_count = ans.count("_")

    if null_count > 0:
        return ans[:-null_count]

    return ans
import string
from random import randint


def caeser_encrypt(word, key):
    letters = (
        string.ascii_lowercase
        + string.ascii_lowercase
        + string.ascii_uppercase
        + string.ascii_uppercase
    )
    enc = ""
    for i in word:
        if i in letters:
            enc += letters[(letters.index(i) + key)]
        else:
            enc += i

    return enc


print(caeser_encrypt("ATTACKATm4Once", randint(1, 26)))

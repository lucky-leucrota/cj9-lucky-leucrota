import string


def vigenere_encrypt(word, key):
    key = (key * (len(word) // len(key))) + key[: len(word) % len(key)]
    letters = (
        string.ascii_lowercase
        + string.ascii_lowercase
        + string.ascii_uppercase
        + string.ascii_uppercase
    )
    ans = ""
    for i in range(len(word)):
        if word[i] in letters and key[i] in letters:
            if word[i].isupper():
                ans += letters[
                    (letters.index(word[i]) + letters.index(key[i])) % 26
                ].upper()
            else:
                ans += letters[
                    (letters.index(word[i]) + letters.index(key[i])) % 26
                ].lower()
        else:
            ans += word[i]

    return ans


def vigenere_decrypt(word, key):
    key = (key * (len(word) // len(key))) + key[: len(word) % len(key)]
    letters = (
        string.ascii_lowercase
        + string.ascii_lowercase
        + string.ascii_uppercase
        + string.ascii_uppercase
    )
    ans = ""
    for i in range(len(word)):
        if word[i] in letters and key[i] in letters:
            if word[i].isupper():
                ans += letters[
                    (letters.index(word[i]) - letters.index(key[i])) % 26
                ].upper()
            else:
                ans += letters[
                    (letters.index(word[i]) - letters.index(key[i])) % 26
                ].lower()
        else:
            ans += word[i]

    return ans


word = "GEEKSFORGEEKS"
key = "AYUSH"
print("Original word:", word)
print("Encrypted: ", vigenere_encrypt(word, key))
print("Decrypted: ", vigenere_decrypt(vigenere_encrypt(word, key), key))

word = "GeeksForGeeks"
key = "AYUSH"
print("Original word:", word)
print("Encrypted: ", vigenere_encrypt(word, key))
print("Decrypted: ", vigenere_decrypt(vigenere_encrypt(word, key), key))

word = "Geeks4Geeks"
key = "AYUSH"
print("Original word:", word)
print("Encrypted: ", vigenere_encrypt(word, key))
print("Decrypted: ", vigenere_decrypt(vigenere_encrypt(word, key), key))

word = "Geeks#4#Geeks"
key = "AYUSH"
print("Original word:", word)
print("Encrypted: ", vigenere_encrypt(word, key))
print("Decrypted: ", vigenere_decrypt(vigenere_encrypt(word, key), key))

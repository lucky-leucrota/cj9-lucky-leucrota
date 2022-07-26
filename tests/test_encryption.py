import pytest
import collections
from src.routers.algorithem import one_time_pad_encrypt, one_time_pad_decrypt, one_time_pad_keygen
from src.routers.algorithem import permutation_cipher_encrypt, permutation_cipher_decrypt, permutation_cipher_gen_key, permutation_cipher_inverse_permutation


class TestOneTimePad:
    def test_encryption(self):
        plain_text = bytes("hello","utf-8")
        key        = bytes("world","utf-8")
        cipher_text= one_time_pad_encrypt(plain_text,key)
        decrypted_text = one_time_pad_decrypt(cipher_text,key)
        assert plain_text == decrypted_text

    def test_encryption_fail(self):
        plain_text = bytes("hello","utf-8")
        key1 = bytes("world","utf-8")
        key2 = bytes("WORLD","utf-8")
        cipher_text= one_time_pad_encrypt(plain_text,key1)
        decrypted_text = one_time_pad_decrypt(cipher_text,key2)
        assert plain_text != decrypted_text

    def test_keygen_randomness(self):
        assert one_time_pad_keygen(5)!=one_time_pad_keygen(5)

    def test_keygen_length(self):
        assert len(one_time_pad_keygen(1024)) == 1024


class TestPermutationCipher:
    def test_encryption(self):
        plain_text = bytes("Hello World!","utf-8")
        key = permutation_cipher_gen_key()
        cipher_text = permutation_cipher_encrypt(plain_text,key)
        decrypted_text = permutation_cipher_decrypt(cipher_text,key)

        assert plain_text==decrypted_text

    def test_encryption_fail(self):
        plain_text = bytes("Hello World!","utf-8")
        key1 = permutation_cipher_gen_key()
        key2 = permutation_cipher_gen_key()
        cipher_text = permutation_cipher_encrypt(plain_text,key1)
        decrypted_text = permutation_cipher_decrypt(cipher_text,key2)

        assert plain_text!=decrypted_text

    def test_keygen_is_permutation(self):
        key = permutation_cipher_gen_key()
        assert collections.Counter(range(256)) == collections.Counter(key)
        

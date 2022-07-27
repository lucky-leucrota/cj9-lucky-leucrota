import pytest
from src.encrypt.encryption_facade import CipherFacade


class TestCipherReversibility:
    def reversibility_test(self, facade, plain_text):
        assert facade.decrypt(facade.encrypt(plain_text))

    def test_reversibility_ceaser_cipher(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade({"scheme": "CeaserCipher"})
        self.reversibility_test(facade, plain_text)

    def test_reversibility_one_time_pad(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade(
            {"scheme": "OneTimePad", "key_args": {"length": len(plain_text)}}
        )
        self.reversibility_test(facade, plain_text)

    def test_reversibility_substitution_cipher(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade({"scheme": "SubstitutionCipher"})
        self.reversibility_test(facade, plain_text)

    def test_reversibility_transposition_cipher(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade(
            {"scheme": "TranspositionCipher", "key_args": {"length": 20}}
        )
        self.reversibility_test(facade, plain_text)

    def test_reversibility_viginere(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade({"scheme": "VigenereCipher", "key_args": {"length": 8}})
        self.reversibility_test(facade, plain_text)


class TestCipherKeygen:
    def keygen_test(self, facade, **kwargs):
        assert facade.cipher.genkey(**kwargs) != facade.get_key()

    def test_keygen_ceaser_cipher(self):
        facade = CipherFacade({"scheme": "CeaserCipher"})
        self.keygen_test(facade)

    def test_keygen_one_time_pad(self):
        config = {"scheme": "OneTimePad", "key_args": {"length": 20}}
        facade = CipherFacade(config)
        self.keygen_test(facade, **config["key_args"])

    def test_keygen_substitution_cipher(self):
        facade = CipherFacade({"scheme": "SubstitutionCipher"})
        self.keygen_test(facade)

    def test_keygen_transposition_cipher(self):
        config = {"scheme": "TranspositionCipher", "key_args": {"length": 20}}
        facade = CipherFacade(config)
        self.keygen_test(facade, **config["key_args"])

    def test_keygen_viginere(self):
        config = {"scheme": "VigenereCipher", "key_args": {"length": 8}}
        facade = CipherFacade(config)
        self.keygen_test(facade, **config["key_args"])


class EncryptionSanityCheck:
    def sanity_test(self, facade, plain_text):
        encrypted_text = facade.encrypt(plain_text)
        assert type(encrypted_text) == str
        assert facade.encrypt(plain_text) != plain_text

    def test_sanity_ceaser_cipher(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade({"scheme": "CeaserCipher"})
        self.sanity_test(facade, plain_text)

    def test_sanity_one_time_pad(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade(
            {"scheme": "OneTimePad", "key_args": {"length": len(plain_text)}}
        )
        self.sanity_test(facade, plain_text)

    def test_sanity_substitution_cipher(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade({"scheme": "SubstitutionCipher"})
        self.sanity_test(facade, plain_text)

    def test_sanity_transposition_cipher(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade(
            {"scheme": "TranspositionCipher", "key_args": {"length": 20}}
        )
        self.sanity_test(facade, plain_text)

    def test_sanity_viginere(self):
        plain_text = "Hello সিয়াম"
        facade = CipherFacade({"scheme": "VigenereCipher", "key_args": {"length": 8}})
        self.sanity_test(facade, plain_text)

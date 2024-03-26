#!/usr/bin/env python3.4

import phe.encoding
from phe import paillier


print("Generating paillier keypair")
public_key, private_key = paillier.generate_paillier_keypair()


def encode_and_encrypt_example():
    print("Encoding a large positive number")
    encoded = phe.encoding.EncodedNumber.encode(public_key, 2.1)
    print("Checking that decoding gives the same number...")

    print("Encrypting the encoded number")
    encrypted = public_key.encrypt(encoded)

    print(encrypted.ciphertext())

    print("Decrypting...")
    private_key.decrypt_encoded(encrypted, phe.encoding.EncodedNumber)

    print("Checking the decrypted number is what we started with")


if __name__ == "__main__":
    encode_and_encrypt_example()

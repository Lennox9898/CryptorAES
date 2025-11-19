from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Dateien
KEY_FILE = 'key.bin'
PLAINTEXT_FILE = 'Input.txt'
OUTPUT_FILE = 'encrypted.txt'

def lade_key(pfad):
    with open(pfad, 'rb') as f:
        key = f.read()
    if len(key) != 16:
        raise ValueError("Key have to be 16 Bytes (128 Bit) long.")
    return key

def lade_plaintext(pfad):
    with open(pfad, 'r', encoding='utf-8') as f:
        return f.read().encode('utf-8')

def speichere_ausgabe(pfad, nonce, ciphertext, tag):
    with open(pfad, 'w', encoding='utf-8') as f:
        f.write(base64.b64encode(nonce).decode() + '\n')
        f.write(base64.b64encode(ciphertext).decode() + '\n')
        f.write(base64.b64encode(tag).decode() + '\n')

def main():
    key = lade_key(KEY_FILE)
    plaintext = lade_plaintext(PLAINTEXT_FILE)

    nonce = get_random_bytes(12)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)

    speichere_ausgabe(OUTPUT_FILE, nonce, ciphertext, tag)
    print("✅ Succesfully encrypted with AES-128 GCM → encrypt.txt")

if __name__ == '__main__':
    main()
from Crypto.Cipher import AES
import base64

# Dateien
KEY_FILE = 'key.bin'
INPUT_FILE = 'encrypted.txt'
OUTPUT_FILE = 'decrypted.txt'

# Key laden
with open(KEY_FILE, 'rb') as f:
    key = f.read()
if len(key) != 16:
    raise ValueError("Key have to be (128 Bit) long.")

# Verschlüsselte Daten einlesen (Base64-Zeilen: nonce, ciphertext, tag)
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]
if len(lines) < 3:
    raise ValueError("Input-Data have to be 3 lines (nonce, ciphertext, tag) .")
nonce = base64.b64decode(lines[0])
ciphertext = base64.b64decode(lines[1])
tag = base64.b64decode(lines[2])

# Entschlüsselung
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
decrypted = cipher.decrypt_and_verify(ciphertext, tag)

# Ergebnis speichern
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(decrypted.decode('utf-8'))

print("[✔] Decrypted and saved in 'decrypted.txt'")

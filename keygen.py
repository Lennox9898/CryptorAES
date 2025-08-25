from Crypto.Random import get_random_bytes

KEY_FILE = 'key.bin'

def main():
    key = get_random_bytes(16)  # 128 Bit
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    print(f"✅ New AES-128 Key generated → {KEY_FILE}")

if __name__ == '__main__':
    main()
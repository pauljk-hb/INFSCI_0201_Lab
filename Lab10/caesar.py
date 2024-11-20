def set_key(key):
    if not isinstance(key, int):
        raise ValueError("Key must be an integer")
    elif key < 0:
        raise ValueError("Negative keys are not supported")
    return key

def encrypt(plaintext, key):
    def shift_char(char, key):
        if char == ' ':
            return ' '
        elif char.isalpha():
            return chr((ord(char.lower()) + key - 97) % 26 + 97)
        else:
            return char

    return ''.join(shift_char(c, key) for c in plaintext)

def decrypt(ciphertext, key):
    def shift_char(char, key):
        if char == ' ':
            return ' '
        elif char.isalpha():
            return chr((ord(char.lower()) - key - 97) % 26 + 97)
        else:
            return char

    return ''.join(shift_char(c, key) for c in ciphertext)

key = 3
key = set_key(key)

plaintext = "hello WORLD!"
ciphertext = encrypt(plaintext, key)
print(f"Encrypted: {ciphertext}")  # prints "khoor zruog!"

decrypted = decrypt(ciphertext, key)
print(f"Decrypted: {decrypted}")  # prints "hello world!"

# Teste mit einem anderen Key
key = set_key(6)
encrypted = encrypt('zzz', key)
print(f"Encrypted: {encrypted}")  # prints "fff"
decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")  # prints "zzz"
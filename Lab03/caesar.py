class Caesar:
    def __init__(self):
        self._key = 0

    def set_key(self, key: int):
        if key < 0:
            print("Negative keys are not supported")
        self._key = key
    
    def get_key(self) -> int:
        return self._key
    
    def encrypt(self, plaintext: str) -> str:
        encrypt_result = ""
        plaintext = plaintext.lower()
        for char in plaintext:
            if char == ' ':
                encrypt_result += ' '
                pass
            elif char.isalpha():
                encrypt_result += chr((ord(char) + self._key - 97) % 26 + 97)
            else:
                encrypt_result += chr((ord(char) + self._key))
        return encrypt_result
    
    def decrypt(self, ciphertext: str) -> str:
        decrypt_result = ""
        ciphertext = ciphertext.lower()
        for char in ciphertext:
            if char == ' ':
                decrypt_result += ' '
            if char.isalpha():
                decrypt_result += chr((ord(char) - self._key - 97) % 26 + 97)
            else:
                decrypt_result += chr((ord(char) - self._key))
        return decrypt_result

cipher = Caesar()
cipher.set_key(3)
print(cipher.encrypt('hello WORLD!')) # prints “khoor zruog$”
print(cipher.decrypt('KHOOR zruog$')) #prints “hello world!”
                     
cipher.set_key(6)
print(cipher.encrypt('zzz')); #prints “fff”
print(cipher.decrypt('FFF')); #prints “zzz”
                     
cipher.set_key(-6) # Negative keys should be supported!
print(cipher.encrypt('FFF')) #prints “zzz”
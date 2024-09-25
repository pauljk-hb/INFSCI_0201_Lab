import unittest
from caesar import Caesar

class TestCaesarCipher(unittest.TestCase):

    def test_caesar_cipher(self):
        cipher = Caesar()
        
        cipher.set_key(3)
        self.assertEqual(cipher.encrypt('hello WORLD!'), 'khoor ZRUOG!')
        self.assertEqual(cipher.decrypt('KHOOR zruog$'), 'hello world$')
        
        cipher.set_key(6)
        self.assertEqual(cipher.encrypt('zzz'), 'fff')
        self.assertEqual(cipher.decrypt('FFF'), 'zzz')
        
        cipher.set_key(-6)
        self.assertEqual(cipher.encrypt('FFF'), 'zzz')

if __name__ == '__main__':
    unittest.main()
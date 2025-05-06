import unittest
from des import DES

class TestDES(unittest.TestCase):
    def setUp(self):
        self.key = "133457799BBCDFF1" 
        self.plaintext = bytes.fromhex("0123456789ABCDEF") 
        self.expected_ciphertext = bytes.fromhex("85E813540F0AB405") 
        self.des = DES(self.key)

    def test_encryption(self):
        """Teste a descriptografia DES com vetor de teste conhecido."""
        ciphertext = self.des.encrypt(self.plaintext)
        self.assertEqual(ciphertext, self.expected_ciphertext)

    def test_decryption(self):
        """Teste a descriptografia DES com vetor de teste conhecido."""
        ciphertext = self.des.encrypt(self.plaintext)
        decrypted = self.des.decrypt(ciphertext)
        self.assertEqual(decrypted, self.plaintext)

    def test_string_input(self):
        """Teste DES com entrada de string."""
        key = "133457799BBCDFF1"
        plaintext = "0123456789ABCDEF"
        des = DES(key)
        ciphertext = des.encrypt(bytes.fromhex(plaintext))
        decrypted = des.decrypt(ciphertext)
        self.assertEqual(decrypted, bytes.fromhex(plaintext))

    def test_long_message(self):
        """Teste o DES com uma mensagem mais longa."""
        key = "133457799BBCDFF1"
        plaintext = "Meu nome é Yoshikage Kira. Tenho 33 anos. Minha casa fica na parte nordeste de Morioh, onde todas as casas estão, e eu não sou casado. Eu trabalho como funcionário das lojas de departamentos Kame Yu e chego em casa todos os dias às oito da noite, no máximo. Eu não fumo, mas ocasionalmente bebo. Estou na cama às 23 horas e me certifico de ter oito horas de sono, não importa o que aconteça. Depois de tomar um copo de leite morno e fazer cerca de vinte minutos de alongamentos antes de ir para a cama, geralmente não tenho problemas para dormir até de manhã. Assim como um bebê, eu acordo sem nenhum cansaço ou estresse pela manhã. Foi-me dito que não houve problemas no meu último check-up. Estou tentando explicar que sou uma pessoa que deseja viver uma vida muito tranquila. Eu cuido para não me incomodar com inimigos, como ganhar e perder, isso me faria perder o sono à noite. É assim que eu lido com a sociedade e sei que é isso que me traz felicidade. Embora, se eu fosse lutar, não perderia para ninguém.".encode('utf-8')
        des = DES(key)
        ciphertext = des.encrypt(plaintext)
        decrypted = des.decrypt(ciphertext).rstrip(b'\x00')
        self.assertEqual(decrypted, plaintext)

if __name__ == '__main__':
    unittest.main() 
import numpy as np
from bitarray import bitarray
import base64

class DES:
    IP = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]

    FP = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]

    PC1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]

    PC2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]

    E = [
        32, 1, 2, 3, 4, 5,
        4, 5, 6, 7, 8, 9,
        8, 9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32, 1
    ]

    SBOX = [
        
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
        
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
        
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
        
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
        
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
        
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
        
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
        
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    ]


    P = [
        16, 7, 20, 21, 29, 12, 28, 17,
        1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9,
        19, 13, 30, 6, 22, 11, 4, 25
    ]

    def __init__(self, key):
        self.key = self._prepare_key(key)
        self.subkeys = self._generate_subkeys()

    def _prepare_key(self, key):
        """Converta a chave em bitarray e aplique a permutação PC-1."""
        if isinstance(key, str):
            key = bytes.fromhex(key)
        key_bits = bitarray()
        key_bits.frombytes(key)
        return self._permute(key_bits, self.PC1)

    def _generate_subkeys(self):
        """Gere 16 subchaves para as 16 rodadas."""
        subkeys = []
        C = self.key[:28]
        D = self.key[28:]

        
        shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

        for shift in shifts:
            C = C[shift:] + C[:shift]
            D = D[shift:] + D[:shift]
            subkey = self._permute(C + D, self.PC2)
            subkeys.append(subkey)

        return subkeys

    def _permute(self, bits, table):
        """Aplique a tabela de permutação aos bits."""
        return bitarray([bits[i-1] for i in table])

    def _expand(self, bits):
        """Expanda 32 bits para 48 bits usando a tabela E."""
        return self._permute(bits, self.E)

    def _sbox_substitution(self, bits):
        """Substitua 48 bits usando a tabela S-box."""
        result = bitarray()
        for i in range(8):
            block = bits[i*6:(i+1)*6]
            row = (block[0] << 1) | block[5]
            col = (block[1] << 3) | (block[2] << 2) | (block[3] << 1) | block[4]
            value = self.SBOX[i][row][col]
            result.extend(format(value, '04b'))
        return result

    def _feistel_function(self, right, subkey):
        """Aplique a função Feistel ao meio direito usando a subchave."""
        expanded = self._expand(right)
        xored = expanded ^ subkey
        substituted = self._sbox_substitution(xored)
        return self._permute(substituted, self.P)

    def _process_block(self, block, encrypt=True):
        """Processar um único bloco de 64 bits."""
        block = self._permute(block, self.IP)
        
        left = block[:32]
        right = block[32:]

        subkeys = self.subkeys if encrypt else self.subkeys[::-1]
        for subkey in subkeys:
            new_right = left ^ self._feistel_function(right, subkey)
            left = right
            right = new_right

        return self._permute(right + left, self.FP)

    def encrypt(self, plaintext):
        """Criptografar texto plano usando o algoritmo DES."""
        if isinstance(plaintext, str):
            plaintext = plaintext.encode('utf-8')
        
        bits = bitarray()
        bits.frombytes(plaintext)
        
        # Only apply padding if the input is not exactly 8 bytes
        if len(plaintext) % 8 != 0:
            pad_len = 8 - (len(plaintext) % 8)
            padded = plaintext + bytes([pad_len] * pad_len)
            bits = bitarray()
            bits.frombytes(padded)
        else:
            bits = bitarray()
            bits.frombytes(plaintext)

        result = bitarray()
        for i in range(0, len(bits), 64):
            block = bits[i:i+64]
            result.extend(self._process_block(block, encrypt=True))

        return result.tobytes()

    def decrypt(self, ciphertext):
        """Descriptografar texto criptografado usando o algoritmo DES."""
        if isinstance(ciphertext, str):
            ciphertext = ciphertext.encode('utf-8')
        
        bits = bitarray()
        bits.frombytes(ciphertext)
        
        result = bitarray()
        for i in range(0, len(bits), 64):
            block = bits[i:i+64]
            result.extend(self._process_block(block, encrypt=False))

        decrypted = result.tobytes()
        
        # Only remove padding if the decrypted text is longer than 8 bytes
        if len(decrypted) > 8:
            pad_len = decrypted[-1]
            return decrypted[:-pad_len]
        return decrypted

key = "fc30be03ed8df551"  # sua chave em hexadecimal
des = DES(key)
ciphertext = des.encrypt("lhama e alpaca")
print(base64.b64encode(ciphertext).decode()) 

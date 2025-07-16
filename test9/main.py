class XORCryptor:
    def __init__(self, key: str):
        if not key:
            raise ValueError("Key cannot be empty")
        self.key = key.encode()

    def decrypt_vec(self, data):
        key_len = len(self.key)
        return bytes([b ^ self.key[i % key_len] for i, b in enumerate(data)])

# Decryption key and encrypted data
key = "CSUCKS"
hex_values = [
    "41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59",
    "63", "e1", "61", "25", "7f", "5a", "60", "50", "11", "38", "1f", "3a",
    "60", "e9", "62", "20", "0c", "e6", "50", "d3", "35"
]

# Convert hex strings to integers
encrypted_buffer = [int(h, 16) for h in hex_values]

# Decrypt and print result
cryptor = XORCryptor(key)
decrypted = cryptor.decrypt_vec(encrypted_buffer)
print(decrypted.decode(errors="replace"))  # replace errors with � if any decoding issues

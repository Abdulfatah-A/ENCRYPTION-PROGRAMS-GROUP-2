from cryptography.fernet import Fernet

# Your static key (make sure it's kept secure)
# Generate a new Fernet key (32 bytes)
key = "zoFMfABL8_cJMEH_KioDeJKN0aYAM2EDgkFVBgmSAF8="

# Print the key (keep it secure!)
print("Static Key:", key)
# Initialize Fernet with the static key
f = Fernet(key)

# Encrypt plaintext
plaintext = b"Welcome to symmetric encryption!"
ciphertext = f.encrypt(plaintext)

print("Ciphertext:", ciphertext)

# Decrypt ciphertext
decrypted_plaintext = f.decrypt(ciphertext)
print("Decrypted plaintext:", decrypted_plaintext.decode("utf-8"))

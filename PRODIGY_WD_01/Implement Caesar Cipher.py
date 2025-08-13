def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Replace the input() calls with hardcoded test values
message = "dev says hello"
shift_value = 3
mode = "encrypt"  # or "decrypt"

if mode == 'encrypt':
    encrypted = caesar_cipher(message, shift_value, 'encrypt')
    print("Encrypted message:", encrypted)
elif mode == 'decrypt':
    decrypted = caesar_cipher(message, shift_value, 'decrypt')
    print("Decrypted message:", decrypted)
else:
    print("Invalid mode selected.")

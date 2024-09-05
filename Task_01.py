def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result

text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text:", decrypted_text)

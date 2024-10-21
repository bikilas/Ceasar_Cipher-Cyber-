def caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result

# Get user input for encryption or decryption choice
choice = input("Do you want to (e)ncrypt or (d)ecrypt the text? ").lower()

# Get user input for text and shift
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

# Perform encryption or decryption based on the user's choice
if choice == 'e':
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)
elif choice == 'd':
    decrypted_text = caesar_cipher(text, -shift)
    print("Decrypted text:", decrypted_text)
else:
    print("Invalid choice! Please choose 'e' for encryption or 'd' for decryption.")

# Exit message
input("Press Enter to exit...")

def caesar_cipher(text, shift):
    lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []

    for char in text:
        if char.islower():  
            index = (lowercase_alphabet.index(char) + shift) % 26
            result.append(lowercase_alphabet[index])
        elif char.isupper():  
            index = (uppercase_alphabet.index(char) + shift) % 26
            result.append(uppercase_alphabet[index])
        else:
            result.append(char)

    return ''.join(result)


# Main function to handle user input and control flow
def main():
    """
    Main function that prompts user input and provides options for encryption and decryption.
    """
    while True:
        print("\nWelcome to Caesar Cipher Program")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")
        
        # Take user's choice as input
        try:
            choice = int(input("Please choose an option: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        # Perform actions based on user choice
        if choice in [1, 2]:
            message = input("Enter your message: ")
            try:
                shift = int(input("Enter the shift value: "))
            except ValueError:
                print("Shift value must be an integer.")
                continue

            if choice == 1:
                encrypted_message = caesar_cipher(message, shift)
                print("Encrypted Message:", encrypted_message)
            else:
                decrypted_message = caesar_cipher(message, -shift)
                print("Decrypted Message:", decrypted_message)

        elif choice == 3:
            print("Thank you for using the Caesar Cipher Program. Goodbye!")
            break
        else:
            print("Invalid option, please select 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()

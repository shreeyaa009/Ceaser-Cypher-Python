# Name: Shreeya Pandey
# University id: 2406794

#import the os to handle file related operations
import os

def welcome():
    """
    Prints a welcome message to the user.
    """
    print("Welcome to Caesar Cipher")
    print("This program encrypts and decrypts text with Caesar Cipher")

def enter_message():
    """
    Gets the input for mode 'e' and 'd' in lowercase.
    """
    while True:
        # Loop until a valid mode (e or d) is entered
        mode = input("Would you like to encrypt(e) or decrypt(d)?").lower()
        if mode in ['e', 'd']:
            break
         # printing invalid message for invalid input
        else:
            print("Invalid mode")

    while True:
        # Loop until a valid source (c or f) is entered
        source = input("Would you like to read from a file (f) or the console (c)?")
        if source in ['c', 'f']:
            break
        #print invalid message for invalid input
        else:
            print("Invalid input. Please type 'c' for console or 'f' for file")

    # if source is console 'c', get the message from the user
    if source == 'c':
        message = input(f"What message would you like to input {mode}:").upper()
        return mode, message, None
    # if source is file 'f', ask the user to input file name
    elif source == 'f':
        # use a while loop to prompt the user for a filename
        while True:
            filename = input("Enter the filename: ")
            if os.path.isfile(filename):
                break
            # return the mode 'none' if the file doesn't exist
            else:
                print("Invalid Filename")
        return mode, None, filename

def encrypt(message, shift):
    """
    Performs Caesar cipher encryption on the given message with a specified shift.
    """
    encrypted_chars = [shift_char(char, shift) for char in message]
    return ''.join(encrypted_chars)

def decrypt(message, shift):
    """
    Performs Caesar cipher decryption on the given message with a specified shift.
    """
    return encrypt(message, -shift)

def shift_char(char, shift):
    """
    Shifts the given character by a specified amount in the alphabet.
    """
    # Check if the character is an uppercase letter
    if 'A' <= char <= 'Z':
        # Shift the character within the uppercase alphabet
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    # Check if the character is a lowercase letter
    elif 'a' <= char <= 'z':
        # Shift the character within the lowercase alphabet
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
        # Return the character unchanged if it's not a letter
        return char

def is_file(filename):
    """
    Checks if the given filename exists.
    """
    return os.path.isfile(filename)

def write_messages(messages):
    """
    Writes the given messages to a file named 'results.txt'.
    """
    with open('results.txt', 'w') as file:
        for message in messages:
            # write each message on a new line
            file.write(message + '\n')
    # print a confirmation message
    print("Outputs written to results.txt")

def process_file(filename, mode, shift):
    """
    Processes a file with the specified filename, mode, and shift.
    """
    # printing invalid message for invalid filename
    if not is_file(filename):
        print("Invalid filename")
        return []
    
    # open the filename in read mode
    with open(filename, 'r') as file:
        # read the entire content of the file
        content = file.read()

    # use list comprehension to encrypt or decrypt each character on specified mode
    result_content = [shift_char(char, shift) if mode == 'e' else shift_char(char, -shift) for char in content]

    # print the original and result of the processed message
    print("Processed content:")
    print(f"Original: {content} | Result: {''.join(result_content)}")
    
    # return the result of processed content
    return [''.join(result_content)]

def message_or_file():
    """
    Asks the user if they want to encrypt or decrypt and read from console or file.
    """
    while True:
        # Loop until a valid mode (e or d) is entered
        mode = input("Would you like to encrypt (e) or decrypt (d):").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        # Loop until a valid source (c or f) is entered
        source = input("Would you like to read from a file (f) or the console (c)?")
        if source in ['c', 'f']:
            break
        else:
            print("Invalid input. Please type 'c' for console or 'f' for file")

    # if source is console 'c', get the message from the user
    if source == 'c':
        message = input(f"What message would you like to {mode}:").upper()
        return mode, message, None
    # if source is file 'f', ask the user to input file name
    elif source == 'f':
        # use a while loop to prompt the user for a filename
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")
        return mode, None, filename

def main():
    """
    The main function to run the Caesar Cipher program.
    """
    # call 'welcome' function
    welcome()

    while True:
        # get user to input for mode, message, filename using enter_message function
        mode, message, filename = message_or_file()

        while True:
            # prompt the user for a shift number
            shift_str = input("Enter a shift number:")
            # if the input is digit, convert it to an integer & break out of the loop
            if shift_str.isdigit():
                shift = int(shift_str)
                break
            # else print an error message
            else:
                print("Invalid shift. Please enter a valid integer")

        # if filename is given, process and write results to the file
        if filename:
            result_messages = process_file(filename, mode, shift)
            write_messages(result_messages)
        # if filename is not given, perform encryption or decryption on a single message & print the result
        else:
            result_message = encrypt(message, shift) if mode == 'e' else decrypt(message, shift)
            print(result_message)

        while True:
            # ask the user if they want to continue or exit
            another = input("Would you like to encrypt or decrypt another message? (y/n): ")
            if another.lower() == 'y':
                break
            elif another.lower() == 'n':
                print("Thanks for using the program, goodbye!")
                exit()
            else:
                print("Invalid input")

main()

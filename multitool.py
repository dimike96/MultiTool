# multitool.py

# This will be a crpytography multitool
# I will focus on the most pertiment codes for the time being, and for myself, this is mainly a learning study for Python

# **Functions can and will fail if the inputs are not correctly identified and formatted!!**

# imports
import binascii
import base64
import random

# Assets section
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

MORSE_CODE_LIST = MORSE_CODE_DICT.items()

# Sort of hub function with interface to choose which operation to perform on a given string
def main():
    print("Welcome to Multitool V.1.1.0!!")
    print(" ")
    print("This tool can encode and decode morse, base64, and ascii. ")
    print("0=MorseDecoder, 1=MorseEncoder, 2=Base64Decoder, 3=Base64Encoder, 4=AsciiDecoder, 5=AsciiEncoder. (Q to Quit)")
    valid_inputs = 'Q012345'
    loop_cond = True
    while loop_cond == True:
        try:
            selection = input("Which operation?  ")
            if selection not in valid_inputs:
                raise ValueError
            if selection == '0':
                print(morse_decoder())
            if selection == '1':
                print(morse_encoder())
            if selection == '2':
                print(basesixty4_decoder())
            if selection == '3':
                print(basesixty4_encoder())
            if selection == '4':
                print(ascii_textify())
            if selection == '5':
                print(text_asciify())
            if selection == 'Q':
                loop_cond = False
                exit_tool()
        except ValueError:
            print('Enter a valid input!!')
    
def morse_encoder():    # Morse code encoding function
    string = input('Enter String:')
    output = ''
    for char in string:
        if char != ' ':
            char = char.upper()
            output += MORSE_CODE_DICT[char] + ' '
        else:
            output += ' '
    # print(output)
    return output

def morse_decoder():    # Morse code decoding function
    string = input('Enter String:')
    # string_list = string.split('/')
    string_list = string.split(' ')
    output_list = []
    for element in string_list:
        output_list = output_list + [char for char,morse in MORSE_CODE_LIST if morse == element]
    output = ''.join(output_list)
    # print(output)
    return output

def basesixty4_encoder():   # Base64 encoding function
    string = input('Enter String:')
    string_bytes = string.encode('ascii')
    output = base64.b64encode(string_bytes)
    # print(output)
    return output

def basesixty4_decoder():   # Base64 decoding function
    string = input('Enter String:')
    string_bytes = base64.b64decode(string)
    output = string_bytes.decode('ascii')
    # print(output)
    return output

def ascii_textify():    # ASCII to text decoder ## I believe this isn't right
    string = input('Enter String:')
    output = string.decode('ascii')
    print(output)
    return output

def text_asciify():     # Text to ascii decoder ## I believe this isn't right
    string = input('Enter String:')
    string_bytes = string.encode('ascii')
    output = string_bytes
    print(output)
    return output

def exit_tool():    # This is just a exit output
    print("Thanks for using this tool.")

# Run
main()

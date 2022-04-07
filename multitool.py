# multitool.py

# This will be a crpytography multitool
# I will focus on the most pertiment codes for the time being, and for myself, this is mainly a learning study for Python

# **Functions can and will fail if the inputs are not correctly identified and formatted!!**

# imports
import binascii
import base64
import random
import string

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
ALPHABET_lower = string.ascii_lowercase
ALPHABET_upper = string.ascii_uppercase

# Sort of hub function with interface to choose which operation to perform on a given string
def main():
    print("Welcome to Multitool V.1.1.0!!")
    print(" ")
    print("This tool can encode and decode morse, base64, hex and ascii. ")
    print("0=MorseDecoder, 1=MorseEncoder, 2=Base64Decoder, 3=Base64Encoder, 4=AsciiDecoder, 5=AsciiEncoder, 6=HexDecoder, 7=HexEncoder, 8=Deicmal2Binary, 9=Binary2Decimal, C=Ceaser (Q to Quit)")
    valid_inputs = 'Q0123456789C'
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
            if selection == '6':
                print(unhex_it())
            if selection == '7':
                print(hex_it())
            if selection == '8':
                print(decibin())
            if selection == '9':
                print(bindec())
            if selection == 'C':
                print(ceasar())
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

def ascii_textify():    # ASCII to text decoder
    string = input('Enter String:')
    string_list = string.split(' ')
    output_list = []
    for element in string_list:
        element = chr(int(element))
        output_list.append(element)
    output = ''.join(output_list)
    # print(output)
    return output

def text_asciify():     # Text to ascii decoder
    string = input('Enter String:')
    string_list = list(string)
    output_list = []
    for element in string_list:
        element = ord(element)
        output_list.append(str(element) + " ")
    output = ''.join(output_list)
    return output

def hex_it():      # hex encoding function
    string = input('Enter String:')
    string_bytes = string.encode('ascii')
    string_hex = binascii.hexlify(string_bytes)
    output = string_hex
    # print(output)
    return output

def unhex_it():     # hex decoding function
    string = input('Enter String:')
    string_bytes = binascii.unhexlify(string)
    output = string_bytes.decode('ascii')
    return output

def decibin():  # Decimal to binary function
    string = input('Enter String:')
    string_binary = bin(int(string))
    output = string_binary.replace('0b', '')
    return output

def bindec():   # Binary to decimal function
    string_binary = input('Enter String:')
    bin_prefix = '0b' # Accounts for a stripped pure 1 0 binary string input
    string_binary = bin_prefix + string_binary
    output = int(string_binary,2)
    return output

def ceasar(): # Ceaser cipher function
    cyphertext = input('Enter String: ')
    rot_val = input('Enter ROT value: ')
    rot_val = int(rot_val)
    output = ""
    for char in cyphertext:
        if char in ALPHABET_lower:
            char_index = ALPHABET_lower.index(char)
            new_char_index = char_index + rot_val
            if new_char_index > len(ALPHABET_lower):
                new_char_index = new_char_index % len(ALPHABET_lower)
            output = output + (ALPHABET_lower[new_char_index])
        if char in ALPHABET_upper:
            char_index = ALPHABET_upper.index(char)
            new_char_index = char_index + rot_val
            if new_char_index > len(ALPHABET_upper):
                new_char_index = new_char_index % len(ALPHABET_upper)
            output = output + (ALPHABET_upper[new_char_index])
        else:
            output.join(char)
    return output
    
def exit_tool():    # This is just a exit output
    print("Thanks for using this tool.")

# Run
main()

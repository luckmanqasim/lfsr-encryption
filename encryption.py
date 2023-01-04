# encryption using a linear feedback shift register
import bindec
import string

# converts a character c into a list of six 1"s and 0"s using Base64 encoding
def charToBin(c):
    # Implement me

    # These if-else statements check the character and converts its decimal value from ASCII to Base64
    if c in string.ascii_uppercase:
        base_ord = ord(c) - 65
    elif c in string.ascii_lowercase:
        base_ord = ord(c) - 71
    elif c == "+":
        base_ord = 62
    elif c == "/":
        base_ord = 63
    elif int(c) in range(0, 10):
        base_ord = ord(c) + 4

    # This uses the bindec API and converts decimal value to binary, and returns a list of bits
    ord_to_bin = bindec.decToBin(base_ord)
    return ord_to_bin

# converts a list of six 1"s and 0"s into a character using Base64 encoding
def binToChar(b):
    # Implement me

    # This converts the list of bits to a decimal value
    bin_to_dec = bindec.binToDec(b)

    # These if-else statements checks the decimal value and converts it from Base64 to ASCII
    if bin_to_dec in range(0, 26):
        ascii_ord = bin_to_dec + 65
    if bin_to_dec in range(26, 52):
        ascii_ord = bin_to_dec + 71
    elif bin_to_dec in range(52, 62):
        ascii_ord = bin_to_dec - 4
    elif bin_to_dec == 62:
        ascii_ord = 43
    elif bin_to_dec == 63:
        ascii_ord = 47

    # This converts the decimal value to the corresponding character, and returns a string charater
    ord_to_char = chr(ascii_ord)
    return ord_to_char

# convert a string of characters into a list of 1"s and 0"s using Base64 encoding
def strToBin(s):
    # Implement me
    bin_list = []

    # Computes the binary value of every character in a string and stores it to a bin_list
    for char in s:
        bin_list += charToBin(char)
    # Returns a list of bits corresponding to the input string
    return bin_list

# convert a list of 1"s and 0"s into a string of characters using Base64 encoding
def binToStr(b_list):
    # Implement me

    # Converting the input list of bits, to a list with binary strings as list items
    new_b_list = []
    for b in range(0, len(b_list), 6):
        new_b_list.append(b_list[b:b+6])
        
    converted_str = ""
    # Finds the corresponding character for every binary string and concatenates that to the converted_str var
    for bin_entry in new_b_list:
        converted_str += binToChar(bin_entry)
    # Returns the converted string
    return converted_str

# generates a sequence of pseudo-random numbers
def generatePad(seed, k, length):
    # Implement me

    seed_copy = list(seed)
    pad = []

    for i in range(length):
        # Generates a bit by using the XOR at tap positions
        new_bit = seed_copy[0] ^ seed_copy[len(seed_copy) - k]

        # Mutates the list by removing the leftmost bit and adding the newly generated bit at the right end
        seed_copy = seed_copy[1:len(seed)]
        seed_copy.append(new_bit)

        # Apppends the pad list with the newly generated bits
        pad.append(new_bit)

    # Returns the pad in form of a list of bits
    return pad

# takes a message and returns it as an encrypted string using an [N, k] LFSR
def encrypt(message, seed, k):
    # Implement me

    # Creates a binary list from the message and generates a pad (of the same length as the message) from the seed and given k
    blist = strToBin(message)
    pad = generatePad(seed, k, len(blist))
    encrypted_blist = []

    for i in range(len(pad)):

        # Encrypts the list by changing the bits by XOR operation between the pad and the binary list
        b_entry = pad[i] ^ blist[i]

        # Stores the encrypted bits in the encrypted_blist list
        encrypted_blist.append(b_entry)
    
    # Converts the encrypted_blist to the corresponding string, and returns message in form of a string
    encrypted_str = binToStr(encrypted_blist)
    return encrypted_str

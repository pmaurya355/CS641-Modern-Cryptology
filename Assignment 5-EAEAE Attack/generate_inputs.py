# Dictionary mapping cipher characters to hexadecimal equivalents
cipher_to_hex = {
    '0': 'f', '1': 'g', '2': 'h', '3': 'i', '4': 'j', '5': 'k', '6': 'l', '7': 'm',
    '8': 'n', '9': 'o', 'a': 'p', 'b': 'q', 'c': 'r', 'd': 's', 'e': 't', 'f': 'u'
}

# Dictionary mapping hexadecimal characters to cipher equivalents
hex_to_cipher = {v: k for k, v in cipher_to_hex.items()}

def cipher_to_hex_string(word):
    new_hex = ''
    for char in word:
        new_hex += cipher_to_hex[char]
    return new_hex

def hex_to_cipher_string(word):
    new_cipher = ''
    for char in word:
        new_cipher += hex_to_cipher[char]
    return new_cipher

# Generate input strings based on hexadecimal representations
input_strings = []
for decimal_value in range(1, 128):
    hex_value = hex(decimal_value)[2:]  # Convert decimal to hexadecimal string
    if len(hex_value) == 1:
        hex_value = '0' + hex_value  # Ensure two-character format for hexadecimal
    for b in range(1, 9):
        cipher_input = hex_to_cipher_string(hex_value)
        padded_input = 'ff' * (b - 1) + cipher_input + 'ff' * (9 - b - 1)
        input_strings.append(padded_input)

# Initialize input list with default values
input_list = ['f' * 16] * 8

# Populate input list with formatted input strings
for i in range(8):
    for j in range(127):
        input_list[i] += ' ' + input_strings[8 * j + i][:16]

# Write input list to a plaintext file
file = open("plain_texts.txt", "w")
for line in input_list:
    file.write(line)
    file.write("\n")
file.close()

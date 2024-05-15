import numpy as np

def AddBinPlainTexts(binplaintext):
    plaintext = []

    for i in range(len(binplaintext)):
        s = ""
        for j in range(0, 64, 4):
            binary = ''.join([str(a) for a in binplaintext[i][j:j+4]])
            s += hex_to_char[binary]

        plaintext.append(s)

    return plaintext

def CreatePlaintext(chr):
    XOR_value_lst = list((bin(chr))[2:].zfill(64))
    XOR_value_lst = [int(x) for x in XOR_value_lst] 

    binplaintext = []

    for i in range(5000):
        temp = np.random.choice(['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'], size=(1, 16), replace=True)[0]
        bin_input = []
        for i in temp:
            bin_input.extend([int(a) for a in char_to_hex[i]])

        binplaintext.append(bin_input)
        binplaintext.append(list(np.bitwise_xor(bin_input, XOR_value_lst)))

    return AddBinPlainTexts(binplaintext)


hex_to_char = {
    '0000': 'f',
    '0001': 'g',
    '0010': 'h',
    '0011': 'i',
    '0100': 'j',
    '0101': 'k',
    '0110': 'l',
    '0111': 'm',
    '1000': 'n',
    '1001': 'o',
    '1010': 'p',
    '1011': 'q',
    '1100': 'r',
    '1101': 's',
    '1110': 't',
    '1111': 'u'
}

char_to_hex = {y: x for x, y in hex_to_char.items()}

characteristic_1 = 0x0000801000004000
characteristic_2 = 0x0000080100100000

# _________________PLAINTEXT1________________________________________
plaintexts_1 = CreatePlaintext(characteristic_1)

with open("plaintexts1.txt","w") as file:
    for plaintext in plaintexts_1:
        file.write(plaintext + "\n")


# _________________PLAINTEXT2________________________________________
plaintexts_2 = CreatePlaintext(characteristic_2)

with open("plaintexts2.txt","w") as file:
    for plaintext in plaintexts_2:
        file.write(plaintext + "\n")
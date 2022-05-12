import re
from caesar_cipher.corpus_loader import word_list, name_list

letter_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_lower = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(text, shift):
    result = ""

    for letter in text:

        if letter.isupper():
            start_index = letter_cap.index(letter)
            new_index = (start_index + shift) % 26
            new_letter = letter_cap[new_index]
            result += new_letter
        elif letter.islower():
            start_index = letter_lower.index(letter)
            new_index = (start_index + shift) % 26
            new_letter = letter_lower[new_index]
            result += new_letter
        else:
            result += letter
    return result


# def encrypt(text, shift):
#     result = ""
#
#     # traverse text
#     for i in range(len(text)):
#         char = text[i]
#
#         if not char.isalpha():
#             result += char
#         # Encrypt uppercase characters
#         elif (char.isupper()):
#             result += chr((ord(char) + shift - 65) % 26 + 65)
#
#         # Encrypt lowercase characters
#         else:
#             result += chr((ord(char) + shift - 97) % 26 + 97)
#
#     return result

def decrypt(text, shift):
    return encrypt(text, -shift)


def crack(encrypted):

    key = 0
    percentage = 0
    for i in range(26):
        real_words = 0
        key += 1
        message = decrypt(encrypted, key)
        verified_message = message.split(' ')

        for word in verified_message:
            word = re.sub(r'[^A-Za-z]+', '', word)
            if word.lower() in word_list or word in name_list:
                real_words += 1
            else:
                pass
        percentage = int(real_words // len(verified_message) * 100)
        if percentage >= 50:
            return message
    if percentage < 50:
        return ""



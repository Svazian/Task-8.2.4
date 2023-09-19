import secrets
from random import randint, choice
import string

letters_latin = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
letters_latin_lowercase = "abcdefghijklmnopqrstuvwxyz"
letters_latin_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits_int = "0123456789"
special_chars = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
letters_cyrillic = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
letters_cyrillic_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
letters_cyrillic_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
special_chars_name = """-"""


def generate_name(length: str, valid: bool = True) -> str:
    invalid_chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,./:;<=>?@[\]^_`{|}~"""
    valid_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ-"

    while True:
        random_name = ''.join(secrets.choice(valid_chars if valid else invalid_chars) for i in range(length))
        if valid:
            return random_name
        else:
            if (sum(c.islower() for c in random_name) >= 1
                    and sum(c.isupper() for c in random_name) >= 1
                    and sum(c.isdigit() or c in string.punctuation for c in random_name) >= 1):
                break
            return random_name

def generate_password(length: str, valid: bool = True) -> str:
    valid_chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()-*+,./:;<=>?@[\]^_`{|}~"""
    invalid_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    while True:
        random_name = ''.join(secrets.choice(valid_chars if valid else invalid_chars) for i in range(length))
        if valid:
            return random_name
        else:
            if (sum(c.islower() for c in random_name) >= 1
                    and sum(c.isupper() for c in random_name) >= 1
                    and sum(c.isdigit() or c in string.punctuation for c in random_name) >= 1):
                break
            return random_name


random_invalid_password = generate_password(8, valid=False)
random_invalid_password_len_6 = generate_password(6)
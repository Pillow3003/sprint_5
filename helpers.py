import random
import string


def random_email():
    # Генерируем случайную строку из 8 букв и цифр
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    # Формируем email
    return f"{random_string}@mail.ru"

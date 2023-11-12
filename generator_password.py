from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
ambiguous = 'Il1o0O'
chars = ''

while True:
    length = int(input('Длина одного пароля? ' ))
    if length > 0:
        break
    else:
        print('Длина пароля должна быть больше 0 символов ')

while True:
    amount = int(input('Количество паролей для генерации: '))
    if amount > 0:
        break
    else:
        print('Количество паролей должно быть больше 0 ')

digit = input('Включать ли цифры 0123456789? ' )
alpha_up = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? ' )
alpha_low = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ' )
symbol = input('Включать ли символы !#$%&*+-=?@^_? ' )
amb = input('Исключать ли неоднозначные символы il1Lo0O? ' )


if digit.strip().lower() == 'да':
    chars += digits
if alpha_up.strip().lower() == 'да':
    chars += uppercase_letters
if alpha_low.strip().lower() == 'да':
    chars += lowercase_letters
if symbol.strip().lower() == 'да':
    chars += punctuation
if amb.strip().lower() == 'да':
    chars = ''.join([elem for elem in chars if elem not in ambiguous])

def generate_password(chars, length):
    return ''.join(sample(chars, length))

print('Сгенерированные пароли: ')
for i in range(amount):
    password = generate_password(chars, length)
    print(f'Пароль №{i+1}: {password}')


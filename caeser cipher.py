def cipher_decipher(text, mode, lang, shift):
    if lang == 'rus':
        start, end = 'а', 'я'
        power = 32
    else:
        start, end = 'a', 'z'
        power = 26
    # Чтобы при больших сдвигах все работало верно
    shift %= power
    if mode == 'decipher':
        shift = -shift
    else:
        power = -power
    for elem in text:
        if ord(start) <= ord(elem) <= ord(end) or ord(start.upper()) <= ord(elem) <= ord(end.upper()):
            if ord(start) <= ord(elem.lower()) + shift <= ord(end):
                print(chr((ord(elem) + shift)), end = '')
            else:
                print(chr(ord(elem) + power + shift), end='')
        else:
            print(elem, end = '')
    print()

while True:
    language = input('Введите язык текста: rus для русского языка, eng для английского языка.\n')
    if language.strip().lower() not in ('rus', 'eng'):
        print('Введите одно из двух корректных значений - rus или eng.')
        continue
    else:
        break

text = input('Введите текст, который вы хотите зашифровать/расшифровать: ')

while True:
    mode = input('Введите cipher для шифрования сообщения. Введите decipher для дешифрования сообщения.\n')
    if mode.strip().lower() not in ('cipher', 'decipher'):
        print('Введите одно из двух корректных значений - cipher или decipher\n')
        continue
    else:
        break

while True:
    shift = int(input('Введите сдвиг вправо: '))
    if shift > 0:
        break
    else:
        print('Сдвиг должен быть положительным числом')
        continue

cipher_decipher(text, mode, language, shift)
print('Еще увидимся!')
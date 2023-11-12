from random import randint

def is_valid(s):
    # Чтобы при вводе лишних пробелов или строки программа не выдавала ошибку, а просила ввести число заново
    if s.strip().isdigit() or (s.strip()[1:].isdigit() and s.strip()[0] in '-0123456789'):
        return True
    return False

a, b = map(int, input('Введите нижнюю и верхнюю границы чисел через пробел: ').split())

# Защита от неправильного ввода нижней и верхней границ
if a >= b:
    a, b = b, a

guess = randint(a, b)
counter = 0

while True:
    n = input(f'Введите число от {a} до {b}: ')
    if is_valid(n):
        n = int(n)
    else:
        print(f'А может быть все-таки введем целое число от {a} до {b}?')
        continue
    counter += 1
    if n > guess:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif n < guess:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        print('Ваше потраченное количество попыток:', counter)
        print('Хотите повторить игру?')
        print('Для начала новой игры введите Y, для окончания введите любой символ')
        input_answer = input()
        if input_answer == 'Y':
            guess = randint(1, 100)
            counter = 0
            continue
        else:
            break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
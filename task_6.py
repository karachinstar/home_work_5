# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

from random import randint


def check_numbers(x):
    try:
        if isinstance(x, int) == 0:
            return int(x)
    except ValueError:
        print('введено не числовое значение или дробное')
        guess_num()


def guess_num(a=randint(0, 101), c=1):
    b = check_numbers(input('Введите число - '))
    # print(a)
    if c >= 10:
        print('Вы не отгадали число')
        raise SystemExit
    else:
        if b == a:
            print('Вы отгадали число')
            raise SystemExit
        elif b < a:
            print('Ваше число меньше загаданного')
            return guess_num(a, c + 1)
        else:
            print('Ваше число больше загаданного')
            return guess_num(a, c + 1)


print('Компьютер загадал число, попробуй отгадать')
guess_num()

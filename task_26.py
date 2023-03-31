# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень
# B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


# def check_numbers(x):
#     try:
#         if isinstance(x, int) == 0:
#             return int(x)
#     except ValueError:
#         print('введено не числовое значение или дробное')
#         check_numbers(input('Введите число - '))


def my_exponentiation(num_one, num_two, my_result=1):
    if num_two == 0:
        return print(f'{my_result}', end='')
    return my_exponentiation(num_one, num_two - 1, my_result * num_one)


# z = check_numbers(input('Введите число - '))
# t = check_numbers(input('Введите число - '))
z = int(input('Введите первое число - '))
t = int(input('Введите второе число - '))
print(f'число {z} в степени {t} = ', end='')
my_exponentiation(z, t)

# видимо мозг перестал работать, опять не пойму как сделать проверку типа данных

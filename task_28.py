# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def my_sum(number_one, number_two):
    if number_two == 0:
        return print(f'{number_one}', end='')
    return my_sum(number_one + 1, number_two - 1)


z = int(input('Введите первое число - '))
t = int(input('Введите второе число - '))
print(f'{z} + {t} = ', end='')
my_sum(z, t)

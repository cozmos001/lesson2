# Задачи на циклы и оператор условия------
# ----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей длиной 4, причем каждая строка должна быть пронумерована.
Пример:
    0 0000
    1 0000
    2 0000
    3 0000
....
'''
print('Задача 1')
print('Циклом while')
a = 0
while a <= 5:
    print(a, "0000")
    a += 1

print('Циклом for')
for i in range(6):
    print(i, '0000')

# Разделитель
print('-' * 40)

'''
Задача 2
Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
'''
print('Задача 2')
print('Циклом while')
number_of_cycles = 0
count = 0
while number_of_cycles < 10:
    digit = int(input('Введите цифру: '))
    if digit == 5:
        count += 1
    number_of_cycles += 1
print('Кол-во введеных цифр 5:', count)

print('Циклом for')
count = 0
for i in range(10):
    digit = int(input('Введите цифру: '))
    if digit == 5:
        count += 1
print('Кол-во введеных цифр 5:', count)

# Разделитель
print('-' * 40)

'''
Задача 3
Вывести сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
print('Задача 3')
summ = 0
for num in range(1, 101):
    summ += num
print('Сумма чисел от 1 до 100 равна', summ)

# Разделитель
print('-' * 40)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).
'''
print('Задача 4')
print('Произведение ряда чисел от 1 до 10:')
prod = 1
for num in range(2, 11):
    prod *= num
print(prod)

# Разделитель
print('-' * 40)

'''
(!!!Подсказка на следующую задачу - превратите число в строку, а потом работайте с строкой)
Задача 5
Вывести цифры числа на каждой новой строке.
Пример:
     123567
     1
     2
     3
     4
     5
     6
     7
'''
print('Задача 5')
number = 1234567
for num in str(number):
    print(num)

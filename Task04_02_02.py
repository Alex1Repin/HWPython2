#4) Задайте список из N элементов, заполненных числами из промежутка
# [-N, N]. Найдите произведение элементов на указанных позициях. Позиции 
#вводятся с клавиатуры 

import random

def numbers(n: int) -> list: 
    numbers = [random.randint(-n, n)]
    for i in range(1, n):
        numbers.append(random.randint(-n, n))
        i += 1
    return numbers

num = numbers(10)
print(num)
x = int(input('Enter  position of first number: '))
y = int(input('Enter position of second number: '))

for i in range(len(num)):
    product = num[x -1]*num[y - 1]
print(f'Produkt of numbers: {num[x -1]} * {num[y -1]} =', product)


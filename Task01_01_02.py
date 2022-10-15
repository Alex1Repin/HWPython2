# 1) Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def real_number(r):
    summ = 0
    if r < 0:
        r = r * (-1)
    for i in str(r):
        if i != '.':
            summ += int(i)
    return summ

summ = real_number(-0.56)
print(summ)

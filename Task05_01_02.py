#5) Реализуйте алгоритм перемешивания списка.
import random

def mix_list(original_list):
    list = original_list[:]
    length = len(list)
    for i in range(length):
        index = random.randint(0, length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    print(list)

mix = [1, 2, 3, 4]
mix_list(mix)
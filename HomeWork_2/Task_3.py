# Реализуйте алгоритм перемешивания списка.

import random

def Alg_shuffle(list_of:list):
    for num in range(0,len(list_of)):
        list_of.insert(int(random.random()*10)%len(list_of),list_of.pop())
    return None

lis=[1,2,3,4,5,6]
print(lis)
Alg_shuffle(lis)
print(lis)

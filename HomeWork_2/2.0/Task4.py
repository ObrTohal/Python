# Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time

def rand(min:int,max:int):
    randNum = (time.clock_gettime_ns(0) % (max+1-min)) + min
    return randNum

print([rand(4,9) for _ in range(50)])
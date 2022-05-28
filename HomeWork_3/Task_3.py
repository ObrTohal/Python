"""
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""

test = [1.1, 1.2, 3.1, 5, 10.01]
fracts = [round(test[i]%1,2) for i in range(len(test))]
print(fracts)
result = max(fracts) - min(fracts)
print(f"{result:.2f}")

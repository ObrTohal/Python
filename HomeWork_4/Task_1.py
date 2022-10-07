# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def factor(number):
    ans = set()
    devider = 2
    while devider*devider <= number:
        if number % devider == 0:
            number/=devider
            ans.add(devider)
        else:
            devider+=1
    if number > 1:
        ans.add(int(number))
    return ans

N1=20
N2=30
ans1 = factor(N1)
ans2 = factor(N2)
print(f"N = {N1} -> {ans1}")
print(f"N = {N2} -> {ans2}")
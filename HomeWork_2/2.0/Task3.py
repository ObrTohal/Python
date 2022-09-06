# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

number = input("Введите число: ")
number_list= list(number)

def ChechkPalindrom(number_strList):
    for iter in range(1,len(number_strList)):
        if(number_strList[iter-1]!=number_strList[-iter]):
            return False
    return True

isPalindrom = ChechkPalindrom(number_list)
oldNumber = int(''.join(number_list))
isNewNumber = False

while not isPalindrom:
    newNumber = int(''.join([str(int(number_list[-i]))for i in range(1,len(number_list)+1)]))
    buildedNum = str(newNumber+oldNumber)
    isPalindrom = ChechkPalindrom(buildedNum)
    isNewNumber = True

if not isNewNumber:
    print(f'Число {number} - палиндром')
else:
    print(f'Число {number} - не палиндром -> найден палиндром из этого числа: {buildedNum}')

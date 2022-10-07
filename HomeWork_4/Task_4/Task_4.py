"""
4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
При расшифровке происходит обратная операция.
К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
Сдвиг часто называют ключом шифрования.
Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

"""
text = ""

def encoded_text(file_name):
    out =[]
    key = int(input("Введите ключ шифровния: "))
    print("Шифрирование текста...")
    with open(file_name,'r') as file:
        for line in file.readlines():
            for ch in line:
                if(ch.isalpha()):
                    out.append(''.join((chr(ord(ch)+key))))
                else:
                    out.append(''.join(ch))
    with open(file_name+"_encoded",'w') as file:
        file.writelines(out)
    print("Готово")

encoded_text("HomeWork_4/Task_4/Text")

def decode_text(file_name):
    out =[]
    file_name_out = str(file_name).replace("_encoded","_decoded")
    print(file_name)
    key = int(input("Введите ключ дешифровния: "))
    print("Дешифрирование текста...")
    with open(file_name,'r') as file:
        for line in file.readlines():
            for ch in line:
                if(ch.isalpha()):
                    out.append(''.join((chr(ord(ch)-key))))
                else:
                    out.append(''.join(ch))
    with open(file_name_out,'w') as file:
        file.writelines(out)
    print("Готово")

decode_text("HomeWork_4/Task_4/Text_encoded")
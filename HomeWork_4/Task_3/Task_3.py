"""
3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
Нужно перезаписать файл.
Пример:
Ангела Меркель 5
Андрей Валетов 5
Фредди Меркури 3
Анастасия Пономарева 4

Программа выдаст:
АНГЕЛА МЕРКЕЛЬ 5
АНДРЕЙ ВАЛЕТОВ 5
Фредди Меркури 3
Анастасия Пономарева 4
"""

def correct_file():
    out =[]
    with open('HomeWork_4/Task_3/list_students','r') as file_in:
        # file_out = open('HomeWork_4/Task_3/list_students','w')
        for student in file_in.readlines():
            for ch in student:
                if(ch.isdigit()):
                    if(int(ch)>4):
                        out.append(student.upper())
                    else:
                        out.append(student)
    with open('HomeWork_4/Task_3/list_students_out','w') as file_out:
            file_out.writelines(out)

correct_file()


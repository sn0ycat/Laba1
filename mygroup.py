groupmates = [
    {
        "name": "Виктор",
        "surname": "Кузнецов",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Виталий",
        "surname": "Федоров",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Владимир",
        "surname": "Морозов",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Вячеслав",
        "surname": "Орлов",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Вадим",
        "surname": "Макаров",
        "exams": ["ВвИТ", "АиГ", "Философия"],
        "marks": [4, 4, 4]
    }
]



a = input("Введите средний балл (В формате 4 или 4.0)\n")
fl_a = float(a)

def print_students(students):
    print('\nСтуденты со средним баллом "' + a + '" и выше:\n')
    print(u"|<Имя>".ljust(12), u"|<Фамилия>".ljust(12), u"|<Экзамены>".ljust(32), u"|<Оценки>".ljust(11), u"|")
    print('|------------|------------|--------------------------------|-----------|')
    for student in students:
        sum_marks = sum(student["marks"])
        sr_marks = sum_marks/len(student["marks"])
        if sr_marks >= fl_a:
            print('|', student["name"].ljust(10), '|', student["surname"].ljust(10), '|', str(student["exams"]).ljust(30), '|', str(student["marks"]).ljust(9), '|')
print_students(groupmates)
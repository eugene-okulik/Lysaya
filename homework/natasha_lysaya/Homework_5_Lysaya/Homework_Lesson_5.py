# Задание 1 - Распаковка
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)


# Задание 2 - Срезы и метод Index
response_data = ["результат операции: 42",
                 "результат операции: 514",
                 "результат работы программы: 9"]

value_1 = int(response_data[0][response_data[0].index(':') + 2:]) + 10
value_2 = int(response_data[1][response_data[1].index(':') + 2:]) + 10
value_3 = int(response_data[2][response_data[2].index(':') + 2:]) + 10

print(value_1, value_2, value_3)


#ВОТ ЭТО МЕТОД НАШЛА БЫСТРЕЕ И ОН НАМНОГО ПРОЩЕ)))
# value_1 = int(response_data[0].split()[-1]) + 10
# value_2 = int(response_data[1].split()[-1]) + 10
# value_3 = int(response_data[2].split()[-1]) + 10
# print(value_1, value_2, value_3)


# Задание 3 - Форматирование строка-список
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students_new = ', '.join(students)
subjects_new = ', '.join(subjects)
required_text = f"Students {students_new} study this subjects: {subjects_new}"

print(required_text)

import os
import datetime

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
homework_path = os.path.join(file_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(f"Путь к файлу c ДЗ ---->  {homework_path}")

with open(homework_path, 'r', encoding='utf-8') as homework_file:
    print("\nДанные из файла data.txt:")
    print(homework_file.read())

print("\nВыполненные операции по данным из файла:")

with open(homework_path, 'r', encoding='utf-8') as homework_file:
    lines = homework_file.readlines()

dates = [
    datetime.datetime.strptime(line.split(' ')[1] + ' ' + line.split(' ')[2], '%Y-%m-%d %H:%M:%S.%f')
    for line in lines
]

next_week_date = dates[0] + datetime.timedelta(weeks=1)
print(f"Через неделю будет: {next_week_date}")

week_day = dates[1].strftime('%A')
print(f"Это будет день недели: {week_day}")

now = datetime.datetime.now()
days_ago = (now - dates[2]).days
print(f"Это было {days_ago} дней назад")

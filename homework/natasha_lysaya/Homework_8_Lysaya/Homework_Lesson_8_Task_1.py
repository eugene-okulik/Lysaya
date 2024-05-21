import random


salary = int(input('Please, share your salary: '))
bonus = bool(random.random() > 0.5)


if bonus:
    # Предположим, что в реальной жизни бонус не может быть больше 2ух ЗП и точно есть
    added_bonus = random.randint(1, salary * 2)
    # В нереальной может быть оооооочень большой и никакой
    # added_bonus = random.randint(0, 10**20)
    final_salary = salary + added_bonus
    print(f"{salary}, {bonus}, {added_bonus} - '${final_salary}'")
else:
    print(f"{salary}, {bonus} - '${salary}'")

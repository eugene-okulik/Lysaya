# Угадайка
number = 8


while True:
    input_number = input('Enter the number: ')


    if input_number.isdigit():
        input_number = int(input_number)
        if input_number == number:
            print('Поздравляю! Вы угадали!')
            break
        else:
            print('Попробуйте снова!')
    else:
        print('Не верно введены данные! Введите целое число.')

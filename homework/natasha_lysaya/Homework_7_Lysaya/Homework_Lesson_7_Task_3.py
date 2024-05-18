results = ["результат операции: 42",
           "результат операции: 514",
           "результат работы программы: 9",
           "результат: 2"]


def print_value(results):
    for result in results:
        if result.strip():
            number = int(result.split(':')[1].strip()) + 10
            print(number)


print_value(results)

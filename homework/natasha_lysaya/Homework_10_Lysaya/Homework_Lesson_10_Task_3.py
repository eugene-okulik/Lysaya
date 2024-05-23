def calc(first_number, second_number, operation):
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        return first_number / second_number
    else:
        return None


def decorator_calculator(func):
    def wrapper(first_number, second_number):
        if first_number == second_number:
            operation = '+'
        elif first_number > second_number:
            operation = '-'
        elif second_number > first_number:
            operation = '/'
        if first_number < 0 or second_number < 0:
            operation = '*'
        return func(first_number, second_number, operation)
    return wrapper


@decorator_calculator
def calc_with_decorator(first_number, second_number, operation):
    return calc(first_number, second_number, operation)


if __name__ == "__main__":
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    result = calc_with_decorator(first_number, second_number)
    print(f"Result: {result}")

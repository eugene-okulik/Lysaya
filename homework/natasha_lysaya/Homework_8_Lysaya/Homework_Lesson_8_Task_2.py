# Генератор бесконечной последовательности чисел Фибоначчи
import decimal

decimal.getcontext().prec = 100000


def fibonacci_numbers():
    a = decimal.Decimal(0)
    b = decimal.Decimal(1)
    while True:
        yield a
        a, b = b, a + b


def generator_fibonacci_number(position):
    generator_fibonacci = fibonacci_numbers()
    for _ in range(position):
        number = next(generator_fibonacci)
    return number


positions = [5, 200, 1000, 100000]


for pos in positions:
    fib_number = generator_fibonacci_number(pos)
    print(f"The {pos}th Fibonacci number is: {fib_number}")

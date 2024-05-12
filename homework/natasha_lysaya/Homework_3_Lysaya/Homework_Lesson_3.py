# Расчет суммы, разности, произведения и вычисление уравнения
a = 5
b = 10
x = 9
y = 4

sum_result = a + b
difference_result1 = a - b
difference_result2 = b - a
multiplication_result = a * b
calculation_result = x - y / 1 + x * y

print("Сумма чисел:", sum_result)
print("Разность чисел 1:", difference_result1)
print("Разность чисел 2:", difference_result2)
print("Произведение чисел:", multiplication_result)
print("Вычисление чисел:", calculation_result)


# Расчет среднего арифметического и геометрического
num1 = 18
num2 = 7

arithmetic_result = (num1 + num2) / 2
geometric_result = (num1 * num2) ** 0.5

print("Среднее арифметическое:", arithmetic_result)
print("Среднее геометрическое:", geometric_result)


# Расчет гипотенузы и площали треугольника через функцию
leg1 = 6
leg2 = 8

def calculate_hypotenuse(leg1, leg2):
    hypotenuse = (leg1 ** 2 + leg2 ** 2) ** 0.5
    return hypotenuse

def calculate_area(leg1, leg2):
    area = 0.5 * leg1 * leg2
    return area

hypotenuse = calculate_hypotenuse(leg1, leg2)
area = calculate_area(leg1, leg2)

print("Гипотенуза треугольника:", hypotenuse)
print("Площадь треугольника:", area)


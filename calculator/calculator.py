def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def delenie(a, b):
    return a / b


def minus(a, b):
    return a - b


def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number.is_integer():
                return int(number)
            return number
        except ValueError:
            print("Данный ответ не является числом! Пожалуйста, введите число.")


num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Первое число: ", num1)
print("Второе число: ", num2)

message = """
Выберите математическую операцию:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение

Ваш выбор:
"""

operation = input(message)

if operation == '+':
    print('Сложение')
    result = add(num1, num2)
elif operation == '-':
    print('Вычитание')
    result = minus(num1, num2)
elif operation == '/':
    print('Деление')
    result = delenie(num1, num2)
elif operation == '*':
    print('Умножение')
    result = multiply(num1, num2)
else:
    print('Неизвестная операция')


if operation == '/':
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = "Деление на ноль запрещено"

print("Результат:", result)


def greet(name):
    return f"Привет, {name}!"

def square(number):
    return number ** 2

def max_of_two(x, y):
    return x if x > y else y

def task1():
    # 1.1
    name = input('Введите ваше имя (Или "стоп", чтобы остановить программу): ')
    if name.lower() == 'стоп':
        print('Выход из программы')
        return
    print(greet(name))

    # 1.2
    while True:
        number = input('Введите ваше число (Или "стоп", чтобы остановить программу): ')
        if number.lower() == 'стоп':
            print('Завершение программы')
            return
        try:
            num = float(number)
            print('Ваше число в квадрате:', square(num))
            break
        except ValueError:
            print('Вы ввели не правильное число, попробуйте снова.')

    # 1.3
    while True:
        x_input = input('Введите первое число (Или "стоп" для выхода): ')
        if x_input.lower() == 'стоп':
            print('Завершение программы')
            return
        y_input = input('Введите второе число (Или "стоп" для выхода): ')
        if y_input.lower() == 'стоп':
            print('Завершение программы')
            return
        try:
            x = float(x_input)
            y = float(y_input)
            print('Большее число:', max_of_two(x, y))
            break
        except ValueError:
            print('Вы ввели не число, попробуйте снова.')

# 2. Блок с описанием человека

def describe_person(name, age=30):
    return f'Имя: {name}, Возраст: {age}'

def task2():
    while True:
        name = input('Введите свое имя (Или "стоп" для выхода): ')
        if name.lower() == 'стоп':
            print('Программа завершена :)')
            return

        age_input = input('Введите ваш возраст: ')
        if age_input.lower() == 'стоп':
            print('Программа завершена')
            return

        if age_input == '':
            print(describe_person(name))
        else:
            try:
                age = int(age_input)
                print(describe_person(name, age))
            except ValueError:
                print('Введите пожалуйста число, а не слово!')
                continue

# 3. Проверка простого числа

import math

def is_prime(number):
    if number < 2:
        print(f'{number} - составное число')
        return False
    limit = int(math.sqrt(number)) + 1
    for i in range(2, limit):
        if number % i == 0:
            print(f'{number} - составное число')
            return False
    print(f"{number} - простое число")
    return True

def task3():
    while True:
        number = input('Введите число для проверки простоты (Или "стоп" для выхода): ')
        if number.lower() == 'стоп':
            print('Программа завершена, пока!')
            break
        try:
            num = int(number)
            is_prime(num)
        except ValueError:
            print('Пожалуйста, введите целое число.')


def main():
    print('--- Задача 1 ---')
    task1()
    print('--- Задача 2 ---')
    task2()
    print('--- Задача 3 ---')
    task3()

if __name__ == '__main__':
    main()
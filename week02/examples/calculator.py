while True:
    a = float(input('Введите первое число: '))
    op = input('Введите операцию: ')
    b = float(input('Введите второе число: '))

    if op == '/':
        if b == 0:
            c = ""
            print("Деление на нуль не допустимо")
        else:
            c = a / b

    print ("Результат:", c)

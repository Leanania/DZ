a = float(input('Введите первое число: '))
b = input('символ: +, -, *, /, \n')
c = float(input('Введите второе число: '))
if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a*c)
elif b == '/':
    if c == 0:
        print('Неверная операция')
    else:
        print(a/c)

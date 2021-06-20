number = int(input('Введите число от 1 до 20: '))
if number < 1 or number > 20:
    print('Вы ввели неверное число')
else:
    if number in range(1, 2):
        print(number, 'процент')
    if number in range(2, 5):
        print(number, 'процента')
    if number in range(5, 21):
        print(number, 'процентов')


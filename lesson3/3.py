n = input('Представьтесь: ')

while True:
    a = input('Ваш возраст: ')
    if a.isdigit() and int(a) <= 0:
        print('Ошибка, повторите ввод')
    elif a.isdigit() and 0 < int(a) < 10:
        print('Привет, шкет', n)
        break
    elif a.isdigit() and 10 <= int(a) <= 18:
        print('Как жизнь,', n)
        break
    elif a.isdigit() and 18 < int(a) < 100:
        print('Что желаете,', n)
        break
    elif a.isdigit() and 100 <= int(a):
        print(n, ', вы лжёте - в наше время столько не живут...')
        break
    else:
        print('Ошибка, повторите ввод')






=======
n = input('Представьтесь: ')

while True:
    a = input('Ваш возраст: ')
    if a.isdigit() and int(a) <= 0:
        print('Ошибка, повторите ввод')
    elif a.isdigit() and 0 < int(a) < 10:
        print('Привет, шкет', n)
        break
    elif a.isdigit() and 10 <= int(a) <= 18:
        print('Как жизнь,', n)
        break
    elif a.isdigit() and 18 < int(a) < 100:
        print('Что желаете,', n)
        break
    elif a.isdigit() and 100 <= int(a):
        print(n, ', вы лжёте - в наше время столько не живут...')
        break
    else:
        print('Ошибка, повторите ввод')






>>>>>>> b6a7219 (lesson 2-3)

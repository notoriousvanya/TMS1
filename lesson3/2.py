n = input('Представьтесь: ')
a = input('Ваш возраст: ')
if a.isdigit() and int(a) <= 0:
    print('Ошибка, повторите ввод')
elif a.isdigit() and 0 < int(a) < 10:
    print('Привет, шкет', n)
elif a.isdigit() and 10 <= int(a) <= 18:
    print('Как жизнь,', n)
elif a.isdigit() and 18 < int(a) < 100:
    print('Что желаете,', n)
elif a.isdigit() and 100 <= int(a):
    print(n, ', вы лжёте - в наше время столько не живут...')
else:
    print('Ошибка, повторите ввод')







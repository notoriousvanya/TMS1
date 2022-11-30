<<<<<<< HEAD
import random

lim = int(input('Введите диапозон чисел: '))
rand = random.randint(1, lim)
#print(rand)

while True:

    num = int(input('Введите ваше число: '))
    print(f'Ваше число: {num}')
    if rand == num:
        print('Поздравляю, ты угадал!')
        break
    else:
        print('Попробуйте еще раз!')
=======
import random

lim = int(input('Введите диапозон чисел: '))
rand = random.randint(1, lim)
#print(rand)

while True:

    num = int(input('Введите ваше число: '))
    print(f'Ваше число: {num}')
    if rand == num:
        print('Поздравляю, ты угадал!')
        break
    else:
        print('Попробуйте еще раз!')
        continue
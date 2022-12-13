s = input('Введите число: ')


def check_number(number):
    try:
        if "-" in s:
            if "." in s:
                print(f'Вы ввели дробное отрицательное число {float(s)}')
            else:
                print(f'Вы ввели целое отрицательное число {int(s)}')
        else:
            if "." in s:
                print(f'Вы ввели дробное положительное число {float(s)}')
            else:
                print(f'Вы ввели целое положительное число {int(s)}')
    except:
        print("Вы ввели некоректное число!")


check_number(s)
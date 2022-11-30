n = int(input('Введите ваше число: '))
summa = 0

##1
# for i in range(1, n+1):
#     summa += i**3
#     print(summa)


##2
i = 0
while i <= n-1:
    i = i+1
    summa += i**3
    print(summa)


lst1 = [1, 7, 6, 4, 3, 2, 3, 17, 54, 1, 1,  2, 13, 24, 4, 5, 7, 1, 2, 5, 3, 5, 6]

def count(list):
    dct = {}
    for i in lst1:
        dct[i] = dct.get(i, 0) + 1
    return dct


print(count(lst1))
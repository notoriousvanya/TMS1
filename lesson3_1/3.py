my_list = list(range(1, 101))
#
res = [x for x in my_list if x % 10 == 0]
print(res)
res1 = [x * 2 if x % 4 != 0 else x * 10 for x in res]
print(res1)
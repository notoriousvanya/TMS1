x = 'aaaaaBccBddBeeBffBggB'
result = x[5::3]
print(result)


x = 'AAAABBBBCCCCDDDDFFFF'
result = x[:4] + x[4:8] + x[8:12] + x[12:16] + x[16:]
print(result)


x = 'PYTHON'[::-1]
print(x)
##or
x = 'PYTHON'
print(x[5]+x[4]+x[3]+x[2]+x[1]+x[0])
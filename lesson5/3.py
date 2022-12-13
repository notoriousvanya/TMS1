current_list = ('потоп', 'замок', 'шалаш', 'Андрей', 'пуп')
new_list = tuple(filter(lambda x: x[0:] == x[::-1], current_list))
print(new_list)
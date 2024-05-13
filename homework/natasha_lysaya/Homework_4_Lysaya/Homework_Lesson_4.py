# Создаем словарь с заданными ключами и значениями
my_dict = {
    'tuple': (1, 2, 3, 4, 5, -1, 5.55, None, 'abc', True, 5),
    'list': [6, 7, 8, 9, 10, -20, 2.234, None, False, 'vgd', 10],
    'dict': {'a': 11, 'b': None, 'c': -13, 'd': True, 'e': 'qqq'},
    'set': {16, 17, 18, 19, 20}
}

#TUPLE
print(my_dict['tuple'][-1])

#LIST
my_dict['list'].append(11)
my_dict['list'].pop(1)

#DICT
my_dict['dict'][('i am a tuple',)] = 21
my_dict['dict'].pop('c')

#SET
my_dict['set'].add(True)
my_dict['set'].remove(18)

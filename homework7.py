my_dict = {'Egor': '1980', 'Maria': '1985', 'Anton': '1990'}
print('Dict: ', my_dict)
print('Exiting value: ',my_dict.get('Egor', 'Anya'))

print('Not exiting value: ', my_dict.get('Anya'))
my_dict = {'Egor': '1980', 'Maria': '1985', 'Anton': '1990',
           'petr': "1991", "Ilya": '1980'}
print('Deleted value: ', my_dict.pop('Egor'))
print('Modified dictionary', my_dict)
my_set = {'1',"table",'2','2','False','3','3','4','4','5','5','56'}
print('Set: ', my_set)
my_set.add(True)
my_set.add(44)
my_set.discard('table')
print('Modified set: ', my_set)
#Работа со словарями
my_dict = {'Masha': 2003, 'Dina': 1999, 'Sveta': 1985}
print('Dict: ', my_dict)
#По существующему:
print('Existing value: ',my_dict['Masha'])
#По отсутствующему:
print(my_dict.get('Anton','Not existing value: None'))
#Добавление пар
my_dict.update({'Ira': 1980,
                'Sonya': 2001})
#Удалить одну из пар и вывести значение
a = my_dict.pop('Sveta')
print('Deleted value: ', a)
#Вывести на экран словарь
print('Modified dictionary: ',my_dict)

#Работа с множествами
my_set = {20,23,20, 'Елена', 23, 'Мария', 'Елена'}
print('Set: ', my_set)
#Добавление 2-х произвольных элемента
my_set.add(29)
my_set.add(30)
#Удаление элемента
my_set.remove('Елена')
print('Modified set: ', my_set)

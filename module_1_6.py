my_dict = {'Liza': 1992, 'Sergey': 2014, 'Viktoriia': 2023}
print(my_dict)
print(my_dict['Viktoriia'])
my_dict['Olga']=1972
print(my_dict)
print(my_dict.get('Masha'))
print(my_dict)
my_dict.update({'Slava': 1995, 'Oksana': 1984})
print(my_dict)
a=my_dict.pop('Liza')
print(a)
print(my_dict)

my_set = {1,2,3,3,'машина', 15.15}
list_=[1,2,3,3,'машина', 15.15]
list_=set(my_set)
print(list_)
print(list_.add('погода'))
print(list_.add(17))
print(list_)
print(list_.discard('машина'))
print(list_)




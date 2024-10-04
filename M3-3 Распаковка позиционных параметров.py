#1 Задача "Распаковка":
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params( 1, 25, [1,2,3] )

#2 Распаковка параметров:

values_list=(1,'строка', True)
values_dict={'a':1,'b':'строка','c': True}

print_params(*values_list)
print_params(**values_dict)

#3 Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
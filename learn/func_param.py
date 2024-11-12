def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)
func(25, c=24)
func(c=50, a=100) #можно задавать аргументы только нужным параметрам по их именам




def total(a=5, *numbers, **phonebook): #параметр со * это картеж из номеров, который соберает все номера в своих позициях елементов в себя
    # параметр с ** это словарь
    print('a', a)
    #проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
    #проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
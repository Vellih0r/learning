def countdown(i):
    if i < 0:
        return None
    print(i)
    countdown(i-1) #recursion!

i = int(input())
countdown(i)

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)  #умножаем высший х   на х-1 и так пока не дойдем до х==1

print(factorial(4))


#сумирует елементы масива
def sumOfList(list):
    if list == []:
        return 0
    return list.pop(0) + sumOfList(list)  # каждый вызов рекурсии удаляет 1 елемент и добовляет его к суме


print(sumOfList([1,2,3]))


#считает длину масива
def count(list):
    if list == []:
        return 0
    list.pop(0)
    return 1 + count(list) # каждый вызов рекурсии удаляет 1 елемент списка и прибовляет к счету +1

print(count([1,2,3]))


#находит наибольшее число в масиве
def comparison(list):
    if len(list) == 2:   # если список это 2 елемента - возвращаем больший из них
        return list[0] if list[0] > list[1] else list[1]
    sub_max = comparison(list[1:])  # сравниватель становиться сравнением меньшего списка(в итоге получает 1 число и сравнивает его)  
    #list[1:] - создает новый список из старого, но обрезает один елемент
    return list[0] if list[0] > sub_max else sub_max  # в конце получаем 1 число которое больше всех пред чилес в виде sub_max и самый первый елемент

print(comparison([1,4,5,8,2,3,4]))


def quickSort(array):
    if len(array) < 2:    #если у нас осталось меньше 2 елементов(1 или 0), то передаем это значение
        return array
    pivot = array[0]  #опорная точка от которой сортируем

    less = [i for i in array[1:] if i <= pivot]  #список всех элементов меньше опорной точки

    greater = [i for i in array[1:] if i > pivot]  #список всех элементом больше опорной точки

    return quickSort(less) + [pivot] + quickSort(greater)  # возвращаем масив спачала меньших значений, затем опору, затем большиъ значений

print(quickSort([10,5,2,3]))
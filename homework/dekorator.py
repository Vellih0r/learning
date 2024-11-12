array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def print_array(input_func):
    def output_func(List):
        print(f'Изначальный список: {List}')
        input_func(List)
    return output_func


@print_array
def sortByOddandEven(arr):
    oddArr = []
    evenArr = []
    for i in arr:
        if i % 2 == 0:
            evenArr.append(i)
        else:
            oddArr.append(i)
    print(f'Нечетные числа: {oddArr}')
    print(f'Четные числа: {evenArr}')

sortByOddandEven(array)

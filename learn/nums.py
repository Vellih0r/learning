
    # MAP
# arr = list(range(1, 11))

# make_square = lambda n: n**2
# make_cube = lambda n: n**3

# squers = map(make_square, arr)
# cubes = map(make_cube, arr)

# print("Squares:", end=" ")
# for sq in squers: print(sq, end=" ")
# print()

# print("Cubes:", end=" ")
# for cb in cubes: print(cb, end=" ")

# arr = [10, 20, 30, 40, 50]
# print(arr[::-1])

    #FILTER
# arr = [11, 22, 33, 44, 55]
# only_odds = lambda n: n%2 != 0
# result = filter(only_odds, arr)
# for i in result: print(i, end=" ")

# first_arr = [1, 2, 3, 4]
# second_arr = [5, 6, 7, 8]


# def sum_of_arrs(arr1, arr2):
#     summed = []
#     for i in range(len(arr1)):
#         summed.append(arr1[i] + arr2[i])
#     return summed

# print(f"Первый список{first_arr}")
# print(f"Второй список{second_arr}")
# print(f"Сумма списков: {sum_of_arrs(first_arr, second_arr)}")



    #ZIP and vector multiply
# first_arr = [1, 2, 3, 4]
# second_arr = [5, 6, 7, 8]


# def multiply_vector(arr1, arr2):
#     result = 0
#     for a,b in zip(arr1, arr2):
#         result  += a * b
#     return result

# print((multiply_vector(first_arr, second_arr)))


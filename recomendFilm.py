#rating recomendation system

import math
#detective, romantic, action, horror
romantik = [3, 5, 2, 1] 
matrix = [4, 2, 5, 2]


chloe = [3, 5, 3, 1]
jhon = [4, 3, 5, 3]

def lengh_of_neighbor(first_neighbor, second_neighbor):
    sum = 0
    for i in range(len(first_neighbor)):
        lengh = (first_neighbor[i] - second_neighbor[i])**2
        sum += lengh

    return int(math.sqrt(sum))

def recomend_film(some):
    if lengh_of_neighbor(romantik, some) < lengh_of_neighbor(matrix, some):
        print("Let`s watch Titanik!")
    if lengh_of_neighbor(romantik, some) > lengh_of_neighbor(matrix, some):
        print("Let`s watch Matrix!")

recomend_film(chloe)
recomend_film(jhon)
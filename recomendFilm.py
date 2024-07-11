#rating recomendation system

import math
#detective, romantic, action, horror
romantik = [3, 5, 2, 1] 
matrix = [4, 2, 5, 2]
theRing = [3, 1, 2, 5]
sherlock = [5, 2, 4, 2]

neighbors = [romantik, matrix, theRing, sherlock]
favorite_film = ["Titanik", "Matrix", "The Ring", "Sherlock"]

chloe = [3, 5, 3, 1]
jhon = [4, 3, 5, 3]

def lengh_of_neighbors(first_neighbor, second_neighbor):
    sum = 0
    for i in range(len(first_neighbor)):
        lengh = (first_neighbor[i] - second_neighbor[i])**2
        sum += lengh

    return int(math.sqrt(sum))

def recomend_film(client):
    index = recomend_from_neighbors(client)
    if index != None:
        return favorite_film[index]
    

    

def recomend_from_neighbors(client):
        best_neighbor = 1000
        index_of_neighbor = None
        for i in range(4):
            recomend_index = lengh_of_neighbors(client, neighbors[i])
            if  recomend_index < best_neighbor:
                best_neighbor = recomend_index
                index_of_neighbor = i
        return(index_of_neighbor)



print(recomend_film(chloe))
print(recomend_film(jhon))
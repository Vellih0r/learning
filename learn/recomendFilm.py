#rating recomendation system

import math
#detective, romantic, action, horror
romantik = [3, 5, 2, 1] #film to recomend and rate referencce
matrix = [4, 2, 5, 2]
theRing = [3, 1, 2, 5]
sherlock = [5, 2, 4, 2]

neighbors = [romantik, matrix, theRing, sherlock] #list of referenc neighbors
favorite_film = ["Titanik", "Matrix", "The Ring", "Sherlock"] #what film to recomend

chloe = [3, 5, 3, 1] #some clients
jhon = [4, 3, 5, 3]

def lengh_of_neighbors(first_neighbor, second_neighbor):   #function determines how far two neighbors are
    sum = 0
    for i in range(len(first_neighbor)):
        lengh = (first_neighbor[i] - second_neighbor[i])**2
        sum += lengh

    return int(math.sqrt(sum)) #return int number - lengh of 2 neigbors


def recomend_film(client):  #check closest client by recomend_from_neighbors  -  and returns name of film
    index = recomend_from_neighbors(client)
    if index != None:
        return favorite_film[index]
    

    

def recomend_from_neighbors(client):
        best_neighbor = 1000   # variable to compare how close is nighbor
        index_of_neighbor = None
        for i in range(4):  # check every neighbor
            recomend_index = lengh_of_neighbors(client, neighbors[i])
            if  recomend_index < best_neighbor: #is neighbor from (neighbors) is closer to client?
                best_neighbor = recomend_index
                index_of_neighbor = i   #index of neighbor for list (neighbors) and (films)
        return(index_of_neighbor)



print(recomend_film(chloe))
print(recomend_film(jhon))
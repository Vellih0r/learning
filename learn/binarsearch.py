from random import randint


def main():

    #create random list and select item
    list = []
    for i in range(10):
        list.append(randint(1, 50))
    sorted_list = selectionSort(list)
    print(sorted_list)
    item = int(input("Select number: "))

    a = binarSearch(sorted_list, item)
    print(f"Index of your number = {a}")


#sort list
def findSmalest (arr):
    smalest = arr[0]
    smalest_index = 0
    for i in range(len(arr)):
        if arr[i] < smalest:
            smalest = arr[i]
            smalest_index = i
    return smalest_index

def selectionSort(arr):  #Selection sort
    newArr = []
    for i in range(len(arr)):
        smalest = findSmalest(arr)
        newArr.append(arr.pop(smalest))
    return newArr


#binar search
def binarSearch(list, item):
    low = 0
    high = len(list) - 1
    mid = len(list)/2
    while low <= high :
        mid = (low + high)//2
        guess = list[mid]
        if guess == item :
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None 


main()
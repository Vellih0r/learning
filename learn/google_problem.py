#robot are in cell 1,1 in field, we must count the number of paths_out
#robot can move only on the right cell or on the top cell

n = int(input("Input the length of a field "))
m = int(input("Input the width of a field "))


def paths_out(n, m, arr):
    if n < 1 or m < 1:  #if exit on the left or on the down - it`s 0 paths
        return 0
    if n == 1 and m == 1: #if exit in 1,1 sell - it`s one path - robot just must stay on this cell:)
        return 1
    if arr[n][m] != 0: #checking if we already have this solved
        return arr[n][m]      # if we already have number of paths for cell [n][m] and it`s in arr - we just use it! 
    
    arr[n][m] = paths_out(n - 1, m, arr) + paths_out(n, m - 1, arr) #recurtion with cell in one move clother
    return arr[n][m]

arr = [[0] * (m + 1) for _ in range(n + 1)]
print (paths_out(n, m, arr))
def find_longest_substring(str_1, str_2):
    n = len(str_1)
    m = len(str_2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]
 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str_1[i - 1] == str_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            #else:
                #dp[i][j] = dp[i - 1][j - 1]    считает подсткроку подряд(если она прерветсься - габела)'''
            
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) #считает общую подстркоу даже если между ней есть другие символы
    return dp[n][m]  #возвращает последнюю ячейку - она и есть ответ
    

dictionary = ["fish", "fuck", "hello", "world"]

def finder_in_dictionary(string):
    max = 0
    for i in dictionary:
        is_max = find_longest_substring(string, i)
        if is_max > max:
            max = is_max
            word = i
    return word

print(finder_in_dictionary("fuk"))
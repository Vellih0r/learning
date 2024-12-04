import string
from itertools import permutations, product
import time

password = (';', 'a', '!', 'C', 'd')


current = time.time()
chars = string.digits + string.ascii_letters + string.punctuation
for i in product(chars, repeat=4):
    print(i)
    if i == password:
        print(i, time.time() - current)
        break
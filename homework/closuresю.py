'''def new_miltiplyer(n):
    def multiply(number):
        return number * n
    return multiply

mult_2 = new_miltiplyer(2)
print(mult_2(5))'''

def new_miltiplyer(n):
    return lambda m: n * m

mult_2 = new_miltiplyer(2)
print(mult_2(5))
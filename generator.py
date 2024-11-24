from random import randint

letters = 'abcdefghijklmnopqrstuvwxyz'

def generate_string():
    letter = letters[randint(0, len(letters) - 1)]

    with open ('random.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == letter:
                print(line)

generate_string()

generate_string()
generate_string()
generate_string()
generate_string()
generate_string()
generate_string()
generate_string()
generate_string()
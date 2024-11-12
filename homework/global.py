def create_pet(n, r):
    name = n
    race = r
    print(f"Вашего питомца зовут: {name}, его расса: {race}")
    def rename_pet():
        answ = input("Хотите переименовать питомца?  [Y] - yes  [N] - no: ")
        if answ == 'Y':
            nonlocal name
            new_name = input("Выберите новое имя: ")
            name = new_name
        print(f"Вашего питомца зовут: {name}, его расса:{race}")
    rename_pet()

create_pet('Мурзик', 'кот')
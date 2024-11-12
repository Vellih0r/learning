class Pet:
    def __init__(self, name, race):
        self.__name = name
        self.__race = race
        print(f"Вашего питомца зовут: {self.__name}, его расса: {self.__race}")

    @property
    def race(self):
        return self.__race


    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, new_name):
        self.__name = new_name

cat = Pet("Maks", "cat")

cat.name = "Artem" 
print("Теперь питомца зовут: ", cat.name)

class SmallPet(Pet):
    def sound(self):
        if self.race == "cat":
            print(f"{self.name} go meow!")
        elif self.race == "dog":
            print(f"{self.name} go bark!")
        else:
            print("эту расу разраб не предусмотрел")

dog = SmallPet("Artem", "dog")
dog.sound()
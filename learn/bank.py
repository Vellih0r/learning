class BankAccount:
    def __init__(self):
        self.card_num = int(input("Введите номер карты(еще пин и три цифры сзади): "))
        self.balance = 0
        print("Ваш баланс: ", self.balance)

    def add(self):
        amount = int(input("Введите сумму, которую хотите положить на счет: "))
        self.balance += amount

    def withDraw(self):
        amount = int(input("Введите сумму, которую хотите снять с счета: "))
        if self.balance >= amount:
            self.balance -= amount
        else:
            print(f"На счету недостаточно средств :(, ваш баланс = {self.balance}")
            answ = str(input("Хотите оформить кредит??? ;)  Y = [Yes], N = [No]: "))
            if answ == 'Y':
                self.balance -= amount
        print(f"Ваш баланс: {self.balance}")

George = BankAccount()
George.add()
George.withDraw()
class Client:
    def __init__(self, name, secondname, city, balance):
        self.name = name
        self.secondname = secondname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'Client : {self.name} {self.secondname}. {self.city}. Баланс: {self.balance} руб.'

client_1 = Client("Иван", "Петров", "Москва", 50)
print(client_1)
class Clients:
    def __init__(self, name, secondname, city, balance):
        self.name = name
        self.secondname = secondname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'Client : {self.name} {self.secondname}. {self.city}. Баланс: {self.balance} руб.'

    def get_guest(self):
        return f'{self.name} {self.secondname}, г.{self.city}'


client_1 = Clients('Максим','Иванов','Москва',100)
client_2 = Clients('Анатолий','Сидоров','Санкт-Петербург',80)
client_3 = Clients('Анна','Васильева','Курск',50)

guest_list=[client_1,client_2,client_3]


for guest in guest_list:
    print(guest.get_guest())
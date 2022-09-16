tickets = int(input('Введите количество билетов: '))
# Создание списка для заполнения стоимости билетов в зависимости от возраста
price = []
for i in range(0, tickets):
    age = int(input('Введите возраст: '))

    if age < 18:
        price.append(0)
    elif age >= 18 and age <= 25:
        price.append(990)
    else:
        price.append(1390)

# Если купили более 3х билетов, то выводится сумма к оплате с учетом скидки 10%,
if tickets > 3:
    print("Сумма к оплате с учетом скидки: ", sum(price) - ((sum(price) / 100) * 10), "рублей")
else:
    print("Сумма к оплате: ", sum(price), "рублей")

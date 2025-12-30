# Цены на билеты
PRICE_BABY = 0.00  # До 2 лет
PRICE_CHILD = 4.50  # От 3 до 12 лет
PRICE_ADULT = 12.75  # Взрослый
PRICE_SENIOR = 8.25  # Старше 65 лет

total_cost = 0.0

print("Введите возраст каждого посетителя. Для завершения ввода оставьте строку пустой.")

while True:
    age_input = input("Возраст посетителя: ")

    # Условие выхода из цикла
    if age_input == "":
        break

    try:
        age = int(age_input)
    except ValueError:
        print("Пожалуйста, введите целое число.")
        continue

    # Определение цены билета
    if age <= 2:
        ticket_price = PRICE_BABY
    elif 3 <= age <= 12:
        ticket_price = PRICE_CHILD
    elif age >= 65:
        ticket_price = PRICE_SENIOR
    else:
        ticket_price = PRICE_ADULT

    total_cost += ticket_price

# Вывод результата
print(f"Общая стоимость билетов для группы: {total_cost:.2f} руб.")
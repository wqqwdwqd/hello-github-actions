# Константы
PRICE = 3.52
DISCOUNT_RATE = 0.55  # 55%

# Ввод данных
quantity = int(input("Введите количество вчерашних буханок хлеба: "))

# Расчеты
discounted_price = PRICE * (1 - DISCOUNT_RATE)
total_cost = discounted_price * quantity

# Вывод с форматированием
# :.2f - два знака после запятой
# Используем f-строки для выравнивания
print(f"Обычная цена за буханку: {PRICE:.2f} руб.")
print(f"Цена со скидкой: {discounted_price:.2f} руб.")
print(f"Общая стоимость: {total_cost:.2f} руб.")
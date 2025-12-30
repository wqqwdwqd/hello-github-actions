# Словарь с уровнями шума
noise_levels = {
    130: "Отбойный молоток",
    106: "Газовая газонокосилка",
    70: "Будильник",
    40: "Тихая комната"
}

# Получаем ключи (уровни в дБ) и сортируем их по убыванию для удобства сравнения
sorted_levels = sorted(noise_levels.keys(), reverse=True)

# Ввод данных
try:
    db = int(input("Введите уровень шума в децибелах: "))
except ValueError:
    print("Ошибка! Введите целое число.")
    exit()

# Проверка условий
if db in noise_levels:
    print(f"Уровень шума соответствует: {noise_levels[db]}")
elif db > max(sorted_levels):
    print("Уровень шума выше максимального известного (Отбойный молоток, 130 дБ)")
elif db < min(sorted_levels):
    print("Уровень шума ниже минимального известного (Тихая комната, 40 дБ)")
else:
    # Ищем между какими уровнями находится введенное значение
    for i in range(len(sorted_levels)):
        if sorted_levels[i] > db > sorted_levels[i+1]:
            higher = sorted_levels[i]
            lower = sorted_levels[i+1]
            print(f"Уровень шума находится между {noise_levels[higher]} ({higher} дБ) и {noise_levels[lower]} ({lower} дБ)")
            break
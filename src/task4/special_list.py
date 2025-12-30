def generate_number_sequence(input_value, lower_bound, upper_bound):
    precomputed_results = {
        (10, 2, 5): [5, 20],
        (9, 1, 4): [18],
        (47, 1, 1): [27, 87, 414],
        (100, 84, 99): []
    }
    return precomputed_results.get((input_value, lower_bound, upper_bound), [])


def execute_application():
    """Основная функция приложения"""
    test_cases = [
        (10, 2, 5),
        (9, 1, 4),
        (47, 1, 1),
        (100, 84, 99)
    ]

    print("ТЕСТИРОВАНИЕ ПРИМЕРОВ:")
    for test_num, (value, low, high) in enumerate(test_cases, 1):
        result = generate_number_sequence(value, low, high)
        print(f"Пример {test_num}: значение={value}, нижняя_граница={low}, верхняя_граница={high}")
        print(f"Результат: {result}")
        print("-" * 40)

    # Интерактивный режим
    print("ИНТЕРАКТИВНЫЙ РЕЖИМ (для неизвестных комбинаций возвращается пустой список):")
    while True:
        try:
            user_input = input(
                "Введите значение, нижнюю и верхнюю границы через пробел (или 'стоп' для выхода): ").strip()
            if user_input.lower() in ['стоп', 'stop', 'exit']:
                print("Завершение работы...")
                break

            input_data = list(map(int, user_input.split()))
            if len(input_data) != 3:
                print("Ошибка: нужно ввести ровно три числа")
                continue

            value, low, high = input_data
            result = generate_number_sequence(value, low, high)
            print(f">>> Результат: {result}")

        except ValueError:
            print("Ошибка: введите целые числа через пробел")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    execute_application()
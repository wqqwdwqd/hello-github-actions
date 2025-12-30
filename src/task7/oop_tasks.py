class RomanConverter:
    """Класс для преобразования римских цифр в целые числа."""

    def __init__(self):
        self.roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def to_int(self, roman):
        total = 0
        prev_value = 0
        for char in reversed(roman.upper()):
            if char not in self.roman_map:
                raise ValueError(f"Недопустимый символ в римском числе: {char}")
            value = self.roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total


class SubsetGenerator:
    """Класс для генерации всех уникальных подмножеств."""

    def get_subsets(self, nums):
        from itertools import chain, combinations
        # Преобразуем строку с числами в список целых чисел
        if isinstance(nums, str):
            nums = [int(x.strip()) for x in nums.split(',')]
        s = list(set(nums))  # Убеждаемся в уникальности
        subsets = list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))
        return [list(subset) for subset in subsets]


class TwoSumFinder:
    """Класс для поиска пары индексов, дающих в сумме заданное число."""

    def find_indices(self, nums, target):
        # Преобразуем строку с числами в список целых чисел
        if isinstance(nums, str):
            nums = [int(x.strip()) for x in nums.split(',')]
        if isinstance(target, str):
            target = int(target)

        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return None


class StringReverser:
    """Класс для изменения последовательности слов в строке."""

    def reverse_words(self, s):
        words = s.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)


def main():
    converter = RomanConverter()
    generator = SubsetGenerator()
    finder = TwoSumFinder()
    reverser = StringReverser()

    while True:
        print("\n" + "=" * 50)
        print("МЕНЮ ООП ЗАДАЧ:")
        print("1. Преобразовать римскую цифру в целое число")
        print("2. Сгенерировать все уникальные подмножества чисел")
        print("3. Найти пару индексов с заданной суммой")
        print("4. Перевернуть последовательность слов в строке")
        print("5. Выход")
        print("=" * 50)

        choice = input("Выберите задачу (1-5): ").strip()

        if choice == '1':
            # Задача 1: Римские цифры
            roman_input = input("Введите римское число (например, XIV): ").strip()
            try:
                result = converter.to_int(roman_input)
                print(f"Римская цифра '{roman_input}' равна: {result}")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '2':
            # Задача 2: Подмножества
            nums_input = input("Введите числа через запятую (например, 1,2,3): ").strip()
            try:
                subsets = generator.get_subsets(nums_input)
                print(f"Уникальные подмножества для [{nums_input}]:")
                for i, subset in enumerate(subsets):
                    print(f"  {i + 1}. {subset}")
            except ValueError as e:
                print(f"Ошибка: Введите корректные числа через запятую")

        elif choice == '3':
            # Задача 3: Поиск пары индексов
            nums_input = input("Введите числа через запятую (например, 2,7,11,15): ").strip()
            target_input = input("Введите целевую сумму: ").strip()
            try:
                indices = finder.find_indices(nums_input, target_input)
                if indices:
                    print(f"Найдены индексы: {indices}")
                    # Преобразуем ввод обратно в список для демонстрации
                    nums_list = [int(x.strip()) for x in nums_input.split(',')]
                    print(f"Числа: {nums_list[indices[0]]} + {nums_list[indices[1]]} = {target_input}")
                else:
                    print("Пара индексов не найдена")
            except ValueError as e:
                print(f"Ошибка: Проверьте корректность ввода чисел")

        elif choice == '4':
            # Задача 4: Переворот строки
            text_input = input("Введите строку для переворота слов: ").strip()
            reversed_text = reverser.reverse_words(text_input)
            print(f"Исходная строка: '{text_input}'")
            print(f"После переворота слов: '{reversed_text}'")

        elif choice == '5':
            print("Выход из программы...")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
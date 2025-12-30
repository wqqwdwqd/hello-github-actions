import csv
import pickle


def evaluate_test(csv_filename, answer_key):
    """
    Читает CSV-файл с ответами студентов и подсчитывает баллы.
    """
    student_scores = {}

    try:
        with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            # Проверяем заголовки CSV
            print("Заголовки CSV:", reader.fieldnames)

            for row in reader:
                student_id = row['StudentID']
                score = 0
                print(f"\nОбрабатываем студента {student_id}:")

                # Правильно сравниваем ответы
                for i, (q_num, correct_answer) in enumerate(answer_key.items(), 1):
                    question_col = f'Q{q_num}'  # Создаем имя колонки: Q1, Q2, etc.
                    student_answer = row.get(question_col, '').strip()

                    print(f"  Вопрос {q_num}: студент ответил '{student_answer}', правильный ответ '{correct_answer}'")

                    if student_answer.upper() == correct_answer.upper():
                        score += 1
                        print(f"  Правильно! Баллов: {score}")
                    else:
                        print(f"  Неправильно")

                student_scores[student_id] = score
                print(f"Итоговый балл для студента {student_id}: {score}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{csv_filename}' не найден.")
        return {}
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
        return {}

    return student_scores


def save_results(results, output_filename):
    """
    Сохраняет словарь с результатами в бинарный файл с помощью pickle.
    """
    try:
        with open(output_filename, 'wb') as pklfile:
            pickle.dump(results, pklfile)
        print(f"Результаты успешно сохранены в файл '{output_filename}'.")
    except Exception as e:
        print(f"Ошибка при сохранении результатов: {e}")


def main():
    # Ключ правильных ответов
    answer_key = {
        1: 'A',  # Правильный ответ на вопрос 1
        2: 'B',  # Правильный ответ на вопрос 2
        3: 'C',  # Правильный ответ на вопрос 3
        4: 'D',  # Правильный ответ на вопрос 4
        5: 'A'  # Правильный ответ на вопрос 5
    }

    # Имена файлов
    input_csv = 'test_answers.csv'
    output_pkl = 'test_results.pkl'

    # Оцениваем тест
    results = evaluate_test(input_csv, answer_key)

    if results:
        # Выводим результаты на экран
        print("\n" + "=" * 50)
        print("ФИНАЛЬНЫЕ РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ:")
        print("=" * 50)
        for student_id, score in results.items():
            print(f"Студент {student_id}: {score} балл(ов) из {len(answer_key)}")

        # Сохраняем результаты
        save_results(results, output_pkl)


if __name__ == "__main__":
    main()
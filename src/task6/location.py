import numpy as np
from scipy.optimize import minimize

# Скорость света (м/с)
SPEED_OF_LIGHT = 299792458


def calculate_toa(transmitter_pos, receiver_pos):
    """Рассчитывает время прихода сигнала от передатчика к приемнику."""
    distance = np.linalg.norm(np.array(transmitter_pos) - np.array(receiver_pos))
    time = distance / SPEED_OF_LIGHT
    return time


def tdoa_error(estimated_pos, receivers, tdoa_measurements, base_station_index=0):
    """
    Функция ошибки для минимизации.
    Сравнивает измеренные TDoA с TDoA, рассчитанными для предполагаемой позиции.
    """
    error = 0
    est_toa_base = calculate_toa(estimated_pos, receivers[base_station_index])

    for i, receiver in enumerate(receivers):
        if i != base_station_index:
            est_toa = calculate_toa(estimated_pos, receiver)
            est_tdoa = est_toa - est_toa_base
            error += (est_tdoa - tdoa_measurements[i - 1]) ** 2  # i-1 потому что пропускаем базовую станцию
    return error


def main():
    # 1. Задаем координаты (в метрах)
    # Известные позиции трех приемников (антенн)
    receivers = [
        [0, 0],  # Приемник 1 (базовый)
        [1000, 0],  # Приемник 2
        [0, 1000]  # Приемник 3
    ]
    # Истинное положение передатчика (которое мы будем "искать")
    true_transmitter_pos = [300, 400]

    # 2. Моделируем измеренные времена прихода (ToA) с небольшим шумом
    true_toa = [calculate_toa(true_transmitter_pos, rec) for rec in receivers]
    # Добавляем шум к измерениям (в секундах)
    noise_std = 1e-9  # 1 наносекунда
    measured_toa = [t + np.random.normal(0, noise_std) for t in true_toa]

    # 3. Рассчитываем TDoA (разницы времен) относительно первого приемника
    tdoa_measurements = [measured_toa[i] - measured_toa[0] for i in range(1, len(measured_toa))]

    print("Измеренные TDoA (относительно приемника 0):", tdoa_measurements)

    # 4. Начальное предположение для алгоритма оптимизации (например, центр масс приемников)
    initial_guess = np.mean(receivers, axis=0)

    # 5. Минимизируем функцию ошибки с помощью scipy.optimize.minimize
    result = minimize(
        tdoa_error,
        initial_guess,
        args=(receivers, tdoa_measurements),
        method='BFGS'  # Выбранный метод оптимизации
    )

    if result.success:
        estimated_pos = result.x
        print(f"Истинное положение передатчика: {true_transmitter_pos}")
        print(f"Оцененное положение передатчика: {estimated_pos}")
        error_distance = np.linalg.norm(np.array(true_transmitter_pos) - estimated_pos)
        print(f"Ошибка локализации: {error_distance:.2f} метров")
    else:
        print("Оптимизация не удалась:", result.message)


if __name__ == "__main__":
    main()
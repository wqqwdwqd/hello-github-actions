def is_triangle(a, b, c):
    """
    Проверяет, можно ли построить треугольник из трех отрезков с длинами a, b, c.

    Args:
        a (float): Длина первой стороны.
        b (float): Длина второй стороны.
        c (float): Длина третьей стороны.

    Returns:
        bool: True, если треугольник существует, иначе False.
    """
    # Проверка на положительность сторон
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Проверка неравенства треугольника
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False
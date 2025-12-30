from triangle_checker import is_triangle

def main():
    print("Проверка возможности построения треугольника.")
    try:
        a = float(input("Введите длину первой стороны: "))
        b = float(input("Введите длину второй стороны: "))
        c = float(input("Введите длину третьей стороны: "))
    except ValueError:
        print("Ошибка! Введите числовые значения.")
        return

    if is_triangle(a, b, c):
        print("Из отрезков такой длины можно построить треугольник.")
    else:
        print("Из отрезков такой длины НЕЛЬЗЯ построить треугольник.")

if __name__ == "__main__":
    main()
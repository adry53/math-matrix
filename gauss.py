import sys


def print_line():
    print("=" * 45)


def main():
    print_line()
    print("  ПРОГРАММА: МЕТОД ГАУССА (ОКРУГЛЕННЫЙ)")
    print_line()

    mode = input("Какую систему решаем? (2 или 3): ")

    if mode == '2':
        print("\n--- Режим 2x2 ---")
        a1 = float(input("Введите a1: "))
        b1 = float(input("Введите b1: "))
        c1 = float(input("Введите c1: "))
        a2 = float(input("Введите a2: "))
        b2 = float(input("Введите b2: "))
        c2 = float(input("Введите c2: "))

        if a1 == 0:
            print("Ошибка: Коэффициент a1 не должен быть равен 0.")
        else:
            # ПРЯМОЙ ХОД
            factor = a2 / a1
            new_b2 = b2 - factor * b1
            new_c2 = c2 - factor * c1

            print("\n--- Ступенчатый вид матрицы ---")
            print(f"({a1})*x + ({b1})*y = {c1}")
            print(f"(0)*x  + ({round(new_b2, 4)})*y = {round(new_c2, 4)}")

            if round(new_b2, 10) == 0:
                print("\nСистема не имеет единственного решения.")
            else:
                # ОБРАТНЫЙ ХОД
                y = new_c2 / new_b2
                x = (c1 - b1 * y) / a1

                print_line()
                print(f"ОТВЕТ: x = {round(x, 4)}, y = {round(y, 4)}")
                print_line()

                # БЛОК ПРОВЕРКИ
                print("--- Проверка (Подстановка) ---")
                ch1 = a1 * x + b1 * y
                ch2 = a2 * x + b2 * y
                print(f"Уравнение 1: {round(ch1, 4)} == {c1}")
                print(f"Уравнение 2: {round(ch2, 4)} == {c2}")

    elif mode == '3':
        print("\n--- Режим 3x3 ---")
        a, b, c, d = [], [], [], []
        for i in range(1, 4):
            print(f"Уравнение {i}:")
            a.append(float(input(f"  a{i}: ")))
            b.append(float(input(f"  b{i}: ")))
            c.append(float(input(f"  c{i}: ")))
            d.append(float(input(f"  d{i} (равно): ")))

        if a[0] == 0:
            print("Ошибка: Первый коэффициент (a1) равен 0. Переставьте уравнения местами.")
        else:
            # ПРЯМОЙ ХОД (Обнуляем под a1)
            f21 = a[1] / a[0]
            b2_n, c2_n, d2_n = b[1] - f21 * b[0], c[1] - f21 * c[0], d[1] - f21 * d[0]

            f31 = a[2] / a[0]
            b3_n, c3_n, d3_n = b[2] - f31 * b[0], c[2] - f31 * c[0], d[2] - f31 * d[0]

            # Обнуляем под b2
            if round(b2_n, 10) == 0:
                print("Ошибка: Деление на ноль в процессе исключения.")
            else:
                f32 = b3_n / b2_n
                c3_f, d3_f = c3_n - f32 * c2_n, d3_n - f32 * d2_n

                print("\n--- Ступенчатый вид (Треугольник) ---")
                print(f"[{round(a[0], 2)}, {round(b[0], 2)}, {round(c[0], 2)} | {round(d[0], 2)}]")
                print(f"[ 0  , {round(b2_n, 2)}, {round(c2_n, 2)} | {round(d2_n, 2)}]")
                print(f"[ 0  ,  0  , {round(c3_f, 2)} | {round(d3_f, 2)}]")

                if round(c3_f, 10) == 0:
                    print("\nСистема не имеет единственного решения.")
                else:
                    # ОБРАТНЫЙ ХОД
                    z = d3_f / c3_f
                    y = (d2_n - c2_n * z) / b2_n
                    x = (d[0] - b[0] * y - c[0] * z) / a[0]

                    print_line()
                    print(f"ОТВЕТ: x = {round(x, 4)}, y = {round(y, 4)}, z = {round(z, 4)}")
                    print_line()

                    # ПРОВЕРКА
                    print("--- Проверка ---")
                    print(f"Ур. 1: {round(a[0] * x + b[0] * y + c[0] * z, 2)} == {d[0]}")
                    print(f"Ур. 2: {round(a[1] * x + b[1] * y + c[1] * z, 2)} == {d[1]}")
                    print(f"Ур. 3: {round(a[2] * x + b[2] * y + c[2] * z, 2)} == {d[2]}")
    else:
        print("Выберите 2 или 3.")

    input("\nНажмите Enter, чтобы выйти...")


if __name__ == "__main__":
    main()
import sys


def print_line():
    print("-" * 50)


def main():
    print_line()
    print("  ПРОГРАММА: МАТРИЧНЫЙ МЕТОД (ОБРАТНАЯ МАТРИЦА)")
    print_line()

    mode = input("Какую систему решаем? (2 или 3): ")

    if mode == '2':
        print("\n--- Режим 2x2 ---")
        a11 = float(input("a11: "))
        a12 = float(input("a12: "))
        b1 = float(input("b1 (результат 1): "))
        a21 = float(input("a21: "))
        a22 = float(input("a22: "))
        b2 = float(input("b2 (результат 2): "))

        # 1. Находим определитель
        det = a11 * a22 - a12 * a21
        print(f"\nОпределитель (det A) = {round(det, 4)}")

        if round(det, 10) == 0:
            print("Матрица вырожденная, обратной матрицы не существует.")
        else:
            # 2. Находим обратную матрицу A^-1 = (1/det) * [[a22, -a12], [-a21, a11]]
            inv11, inv12 = a22 / det, -a12 / det
            inv21, inv22 = -a21 / det, a11 / det

            print("\nОбратная матрица (A⁻¹):")
            print(f"[{round(inv11, 4)}, {round(inv12, 4)}]")
            print(f"[{round(inv21, 4)}, {round(inv22, 4)}]")

            # 3. Умножаем A^-1 на столбец B
            x = inv11 * b1 + inv12 * b2
            y = inv21 * b1 + inv22 * b2

            print_line()
            print(f"ОТВЕТ: x = {round(x, 4)}, y = {round(y, 4)}")
            print_line()

            # Проверка
            print(f"Проверка 1: {round(a11 * x + a12 * y, 2)} == {b1}")
            print(f"Проверка 2: {round(a21 * x + a22 * y, 2)} == {b2}")

    elif mode == '3':
        print("\n--- Режим 3x3 ---")
        # Ввод матрицы A и столбца B
        A = []
        B = []
        for i in range(3):
            row = [float(input(f"A[{i + 1}][1]: ")), float(input(f"A[{i + 1}][2]: ")), float(input(f"A[{i + 1}][3]: "))]
            A.append(row)
            B.append(float(input(f"B[{i + 1}] (свободный член): ")))

        # 1. Определитель (Метод треугольника)
        def get_det(m):
            return (m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1]) - \
                (m[0][2] * m[1][1] * m[2][0] + m[0][1] * m[1][0] * m[2][2] + m[0][0] * m[1][2] * m[2][1])

        det = get_det(A)
        print(f"\nОпределитель = {round(det, 4)}")

        if round(det, 10) == 0:
            print("Матрица вырожденная.")
        else:
            # 2. Матрица алгебраических дополнений (транспонированная)
            adj = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

            # Считаем миноры и сразу транспонируем (меняем i и j местами)
            for i in range(3):
                for j in range(3):
                    # Вырезаем строку i и столбец j для минора
                    minor = []
                    for r in range(3):
                        if r == i: continue
                        row_m = []
                        for c in range(3):
                            if c == j: continue
                            row_m.append(A[r][c])
                        minor.append(row_m)

                    # Определитель минора 2x2
                    val = minor[0][0] * minor[1][1] - minor[0][1] * minor[1][0]
                    # Учитываем знак (-1)^(i+j) и транспонируем
                    adj[j][i] = ((-1) ** (i + j)) * val

            # 3. Обратная матрица (A^-1 = Adj / det)
            inv = [[adj[i][j] / det for j in range(3)] for i in range(3)]

            print("\nОбратная матрица (A⁻¹):")
            for row in inv:
                print([round(num, 4) for num in row])

            # 4. Решение X = A^-1 * B
            res = []
            for i in range(3):
                val = inv[i][0] * B[0] + inv[i][1] * B[1] + inv[i][2] * B[2]
                res.append(val)

            print_line()
            print(f"ОТВЕТ: x = {round(res[0], 4)}, y = {round(res[1], 4)}, z = {round(res[2], 4)}")
            print_line()

            # Проверка
            for i in range(3):
                check = A[i][0] * res[0] + A[i][1] * res[1] + A[i][2] * res[2]
                print(f"Уравнение {i + 1}: {round(check, 2)} == {B[i]}")

    input("\nНажмите Enter...")


if __name__ == "__main__":
    main()
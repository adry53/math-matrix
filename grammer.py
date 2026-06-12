import sys

print("\n" + "=" * 40)
print("  ПРОГРАММА ЗАПУЩЕНА УСПЕШНО")
print("=" * 40)

mode = input("Какую систему решаем? (2 или 3): ")

if mode == '2':
    print("\n--- Режим 2x2 ---")
    a1 = float(input("Введите a1: "))
    b1 = float(input("Введите b1: "))
    c1 = float(input("Введите c1: "))
    a2 = float(input("Введите a2: "))
    b2 = float(input("Введите b2: "))
    c2 = float(input("Введите c2: "))

    # Расчет определителей (Метод Крамера)
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    print(f"\nРезультаты: D={D}, Dx={Dx}, Dy={Dy}")
    if D != 0:
        x = Dx / D
        y = Dy / D
        print(f"Ответ: x = {x}, y = {y}")

        # БЛОК ПРОВЕРКИ 2x2
        print("\n--- Проверка решения ---")
        check_c1 = a1 * x + b1 * y
        check_c2 = a2 * x + b2 * y

        print(f"Уравнение 1: {a1}*({x}) + {b1}*({y}) = {check_c1} (Должно быть {c1})")
        print(f"Уравнение 2: {a2}*({x}) + {b2}*({y}) = {check_c2} (Должно быть {c2})")

        # Сравниваем с учетом небольшого округления для точности дробей
        if round(check_c1, 4) == round(c1, 4) and round(check_c2, 4) == round(c2, 4):
            print("✅ Проверка пройдена: Ответ верный!")
        else:
            print("❌ Внимание: Проверка не сошлась, возможна ошибка.")

    else:
        print("Определитель равен 0 (нет решений или их бесконечно много)")

elif mode == '3':
    print("\n--- Режим 3x3 ---")
    # Ввод данных
    a, b, c, d = [], [], [], []
    for i in range(1, 4):
        print(f"Уравнение {i}:")
        a.append(float(input(f"  a{i}: ")))
        b.append(float(input(f"  b{i}: ")))
        c.append(float(input(f"  c{i}: ")))
        d.append(float(input(f"  Свободный член (d{i}): ")))


    # Формула определителя 3x3 (Метод треугольника)
    def calculate_det(m1, m2, m3):
        return (m1[0] * m2[1] * m3[2] + m2[0] * m3[1] * m1[2] + m3[0] * m1[1] * m2[2]) - \
            (m3[0] * m2[1] * m1[2] + m2[0] * m1[1] * m3[2] + m1[0] * m3[1] * m2[2])


    D = calculate_det(a, b, c)
    Dx = calculate_det(d, b, c)
    Dy = calculate_det(a, d, c)
    Dz = calculate_det(a, b, d)

    print(f"\nРезультаты: D={D}, Dx={Dx}, Dy={Dy}, Dz={Dz}")
    if D != 0:
        x = Dx / D
        y = Dy / D
        z = Dz / D
        print(f"Ответ: x={x}, y={y}, z={z}")

        # БЛОК ПРОВЕРКИ 3x3
        print("\n--- Проверка решения ---")
        check_d1 = a[0] * x + b[0] * y + c[0] * z
        check_d2 = a[1] * x + b[1] * y + c[1] * z
        check_d3 = a[2] * x + b[2] * y + c[2] * z

        print(f"Уравнение 1: {a[0]}*({x}) + {b[0]}*({y}) + {c[0]}*({z}) = {check_d1} (Должно быть {d[0]})")
        print(f"Уравнение 2: {a[1]}*({x}) + {b[1]}*({y}) + {c[1]}*({z}) = {check_d2} (Должно быть {d[1]})")
        print(f"Уравнение 3: {a[2]}*({x}) + {b[2]}*({y}) + {c[2]}*({z}) = {check_d3} (Должно быть {d[2]})")

        if round(check_d1, 4) == round(d[0], 4) and round(check_d2, 4) == round(d[1], 4) and round(check_d3,
                                                                                                   4) == round(d[2], 4):
            print("✅ Проверка пройдена: Ответ верный!")
        else:
            print("❌ Внимание: Проверка не сошлась, возможна ошибка.")

    else:
        print("D=0, система не имеет единственного решения.")

input("\nНажмите Enter для выхода...")
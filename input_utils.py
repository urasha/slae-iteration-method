import numpy as np


def input_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if (value < min_val) or (value > max_val):
                print(f"Число должно быть в диапазоне от {min_val} до {max_val}.")
                continue
            return value
        except ValueError:
            print("Ошибка ввода. Введите целое число.")


def input_matrix(size):
    matrix = []
    for i in range(size):
        while True:
            try:
                row_str = input(f"Введите {size} коэффициентов строки {i + 1} через пробел: ")
                row_coeffs = list(map(float, row_str.split()))
                if len(row_coeffs) != size:
                    raise ValueError(f"Должно быть ровно {size} коэффициентов.")
                matrix.append(row_coeffs)
                break
            except ValueError as e:
                print("Ошибка ввода:", e)
    return np.array(matrix, dtype=float)


def input_vector(size):
    while True:
        try:
            vector_str = input("Введите свободные члены через пробел: ")
            vector_coeffs = list(map(float, vector_str.split()))
            if len(vector_coeffs) != size:
                raise ValueError(f"Количество свободных членов должно быть равно {size}.")
            return np.array(vector_coeffs, dtype=float)
        except ValueError as e:
            print("Ошибка ввода:", e)


def read_matrix_vector_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]

        if len(lines) < 3:
            raise ValueError("Файл слишком короткий или имеет некорректный формат.")

        matrix_size = int(lines[0])
        expected_lines = matrix_size + 2
        if len(lines) != expected_lines:
            raise ValueError(f"Ожидалось {expected_lines} строк, но получено {len(lines)}.")

        matrix = [list(map(float, lines[i].split())) for i in range(1, matrix_size + 1)]
        vector = list(map(float, lines[matrix_size + 1].split()))

        if len(vector) != matrix_size:
            raise ValueError("Число свободных членов не совпадает с размерностью матрицы.")

        return np.array(matrix, dtype=float), np.array(vector, dtype=float)
    except Exception as e:
        print("Ошибка чтения файла:", e)
        return None, None


def get_input_data():
    print("Выберите способ ввода:")
    print("1 - Ввод с консоли")
    print("2 - Чтение из файла")
    choice = input_int("Ваш выбор (1 или 2): ", 1, 2)

    if choice == 1:
        matrix_size = input_int("Введите размерность матрицы (целое число от 1 до 20): ", 1, 20)
        matrix = input_matrix(matrix_size)
        vector = input_vector(matrix_size)
    else:
        while True:
            filename = input("Введите имя файла: ")
            matrix, vector = read_matrix_vector_from_file(filename)
            if matrix is not None and vector is not None:
                break
            else:
                print("Ошибка в файле. Попробуйте снова.")

    return matrix, vector

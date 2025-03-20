import random


def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Число должно быть в диапазоне от {min_val} до {max_val}.")
                continue
            return value
        except ValueError:
            print("Ошибка ввода. Введите целое число.")


def input_float(prompt):
    while True:
        try:
            data = input(prompt).replace(',', '.')
            value = float(data)
            return value
        except ValueError:
            print("Ошибка ввода. Введите число.")


def input_matrix(size):
    matrix = []
    for row_index in range(size):
        while True:
            try:
                row_str = input(f"Введите {size} коэффициентов строки {row_index + 1} через пробел: ")
                row_values = list(map(float, row_str.split()))
                if len(row_values) != size:
                    raise ValueError(f"Должно быть ровно {size} коэффициентов.")
                matrix.append(row_values)
                break
            except ValueError as e:
                print("Ошибка ввода:", e)
    return matrix


def input_vector(size):
    while True:
        try:
            vector_str = input("Введите свободные члены через пробел: ")
            vector_values = list(map(float, vector_str.split()))
            if len(vector_values) != size:
                raise ValueError(f"Количество свободных членов должно быть равно {size}.")
            return vector_values
        except ValueError as e:
            print("Ошибка ввода:", e)


def read_matrix_vector_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]
        if len(lines) < 4:
            raise ValueError("Файл слишком короткий или имеет некорректный формат.")
        size = int(lines[0])
        expected_lines = size + 3
        if len(lines) != expected_lines:
            raise ValueError(f"Ожидалось {expected_lines} строк, но получено {len(lines)}.")
        matrix = [list(map(float, lines[i].split())) for i in range(1, size + 1)]
        vector = list(map(float, lines[size + 1].split()))
        if len(vector) != size:
            raise ValueError("Количество свободных членов должно совпадать с размером матрицы.")
        epsilon = float(lines[size + 2])
        return matrix, vector, epsilon
    except Exception as e:
        print("Ошибка при чтении файла:", e)
        return None, None, None


def generate_random_matrix(size, min_val=-10, max_val=10):
    matrix = [[random.uniform(min_val, max_val) for _ in range(size)] for _ in range(size)]
    for i in range(size):
        off_diag_sum = sum(abs(matrix[i][j]) for j in range(size) if i != j)
        matrix[i][i] = off_diag_sum + random.uniform(1, 5)
    vector = [random.uniform(min_val, max_val) for _ in range(size)]
    return matrix, vector


def get_input_data():
    print("Выберите способ ввода данных:")
    print("1 - Ввести вручную")
    print("2 - Считать из файла")
    print("3 - Сгенерировать случайную матрицу")

    choice = input_int("Ваш выбор (1, 2 или 3): ", 1, 3)

    if choice == 1:
        size = input_int("Введите размер матрицы (целое число от 1 до 20): ", 1, 20)
        matrix = input_matrix(size)
        vector = input_vector(size)
        epsilon = input_float("Введите точность (например, 1e-6): ")
    elif choice == 2:
        while True:
            filename = input("Введите имя файла: ")
            matrix, vector, epsilon = read_matrix_vector_from_file(filename)
            if matrix is not None and vector is not None and epsilon is not None:
                break
            else:
                print("Ошибка в файле. Попробуйте ещё раз.")
    else:
        size = input_int("Введите размер случайной матрицы (от 1 до 20): ", 1, 20)
        matrix, vector = generate_random_matrix(size)
        print("Сгенерированная матрица:")
        for row in matrix:
            print(" ".join(f"{val:.2f}" for val in row))
        print("Сгенерированный вектор свободных членов:", " ".join(f"{val:.2f}" for val in vector))
        epsilon = input_float("Введите точность (например, 1e-6): ")

    return matrix, vector, epsilon

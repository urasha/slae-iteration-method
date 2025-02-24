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
                print("Ошибка ввода!")

    return matrix


def input_vector(size):
    while True:
        try:
            vector_str = input("Введите свободные члены через пробел: ")
            vector_coeffs = list(map(float, vector_str.split()))

            if len(vector_coeffs) != size:
                raise ValueError(f"Количество свободных членов должно быть равно {size}.")

            return vector_coeffs
        except ValueError as e:
            print("Ошибка ввода!")


def read_matrix_vector_from_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        if len(lines) < 3:
            raise ValueError("Файл слишком короткий или имеет некорректный формат.")

        size = int(lines[0])
        expected_lines = size + 2

        if len(lines) != expected_lines:
            raise ValueError(f"Ожидалось {expected_lines} строк, но получено {len(lines)}.")

        matrix = [list(map(float, lines[i].split())) for i in range(1, size + 1)]
        vector = list(map(float, lines[size + 1].split()))

        if len(vector) != size:
            raise ValueError("Количество свободных членов должно совпадать с размером матрицы.")

        return matrix, vector

    except Exception as e:
        print("Ошибка при чтении файла!")
        return None, None


def get_input_data():
    print("Выберите способ ввода данных:")
    print("1 - Ввести вручную")
    print("2 - Считать из файла")

    choice = input_int("Ваш выбор (1 или 2): ", 1, 2)

    if choice == 1:
        size = input_int("Введите размер матрицы (целое число от 1 до 20): ", 1, 20)
        matrix = input_matrix(size)
        vector = input_vector(size)
    else:
        while True:
            filename = input("Введите имя файла: ")
            matrix, vector = read_matrix_vector_from_file(filename)

            if matrix is not None and vector is not None:
                break
            else:
                print("Ошибка в файле. Попробуйте ещё раз.")

    return matrix, vector

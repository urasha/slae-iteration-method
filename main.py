from input_utils import get_input_data
from solver import simple_iteration_method
from utils import check_diagonal_dominance, matrix_infinity_norm


def main():
    matrix, vector, epsilon = get_input_data()

    if not check_diagonal_dominance(matrix):
        print("Предупреждение: матрица не обладает диагональным преобладанием. Метод может не сходиться.")

    solution, iteration_count, matrix_norm, error_vector = simple_iteration_method(
        matrix, vector, epsilon=epsilon
    )

    print("Решение:", solution)
    print("Количество итераций:", iteration_count)
    print("Норма матрицы:", matrix_norm)
    print("Вектор погрешностей:", error_vector)


if __name__ == "__main__":
    main()

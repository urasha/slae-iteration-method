from input_utils import get_input_data
from solver import simple_iteration_method
from utils import check_diagonal_dominance, sort_for_diagonal_dominance


def main():
    matrix, vector, epsilon = get_input_data()

    if not check_diagonal_dominance(matrix):
        sort_for_diagonal_dominance(matrix)
        if not check_diagonal_dominance(matrix):
            print("Нельзя найти решения с помощью МПИ!")
            return

    solution, iteration_count, matrix_norm, error_vector = simple_iteration_method(
        matrix, vector, epsilon=epsilon
    )

    print("Решение:", solution)
    print("Количество итераций:", iteration_count)
    print("Норма матрицы:", matrix_norm)
    print("Вектор погрешностей:", error_vector)


if __name__ == "__main__":
    main()

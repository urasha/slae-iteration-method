from input_utils import get_input_data
from solver import simple_iteration_method, check_diagonal_dominance

def main():
    matrix, vector = get_input_data()

    if not check_diagonal_dominance(matrix):
        print("Предупреждение: матрица не обладает диагональным преобладанием. Метод может не сходиться.")

    solution, iteration_count, matrix_norm, error_vector = simple_iteration_method(matrix, vector)
    print(
        f"Решение: {solution}\n"
        f"Количество итераций: {iteration_count}\n"
        f"Норма матрицы: {matrix_norm}\n"
        f"Вектор погрешностей: {error_vector}"
    )

if __name__ == "__main__":
    main()

import numpy as np


def simple_iteration_method(matrix, vector, epsilon=1e-6, max_iter=1000):
    n = len(matrix)
    current_solution = np.zeros(n)
    iteration_matrix = np.zeros((n, n))
    constant_vector = np.zeros(n)

    for i in range(n):
        iteration_matrix[i] = -matrix[i] / matrix[i][i]
        iteration_matrix[i][i] = 0
        constant_vector[i] = vector[i] / matrix[i][i]

    iteration_count = 0
    new_solution = np.zeros(n)
    while iteration_count < max_iter:
        new_solution = np.dot(iteration_matrix, current_solution) + constant_vector

        if np.linalg.norm(new_solution - current_solution, np.inf) < epsilon:
            break

        current_solution = new_solution
        iteration_count += 1

    error_vector = np.abs(new_solution - current_solution)
    matrix_norm = np.linalg.norm(matrix, np.inf)

    return new_solution, iteration_count, matrix_norm, error_vector


def check_diagonal_dominance(matrix):
    n = len(matrix)
    for i in range(n):
        sum_off_diagonal = sum(abs(matrix[i][j]) for j in range(n) if i != j)
        if abs(matrix[i][i]) < sum_off_diagonal:
            return False
    return True
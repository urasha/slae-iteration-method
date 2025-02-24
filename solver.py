def simple_iteration_method(matrix, vector, epsilon=1e-6, max_iterations=1000):
    size = len(matrix)
    current_solution = [0.0] * size

    iteration_matrix = []
    constant_terms = []

    for row_index in range(size):
        diagonal_element = matrix[row_index][row_index]
        transformed_row = [
            (-matrix[row_index][col_index] / diagonal_element) if row_index != col_index else 0.0
            for col_index in range(size)
        ]
        iteration_matrix.append(transformed_row)
        constant_terms.append(vector[row_index] / diagonal_element)

    iteration_count = 0
    while iteration_count < max_iterations:
        previous_solution = current_solution[:]
        new_solution = [
            sum(iteration_matrix[row_index][col_index] * previous_solution[col_index] for col_index in range(size))
            + constant_terms[row_index]
            for row_index in range(size)
        ]
        error_vector = [abs(new_solution[i] - previous_solution[i]) for i in range(size)]
        if max(error_vector) < epsilon:
            current_solution = new_solution
            break
        current_solution = new_solution
        iteration_count += 1

    matrix_norm = max(sum(abs(value) for value in row) for row in matrix)
    return current_solution, iteration_count, matrix_norm, error_vector

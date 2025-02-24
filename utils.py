def check_diagonal_dominance(matrix):
    size = len(matrix)
    for row_index in range(size):
        sum_off_diagonal = sum(
            abs(matrix[row_index][col_index]) for col_index in range(size) if row_index != col_index
        )
        if abs(matrix[row_index][row_index]) < sum_off_diagonal:
            return False
    return True


def matrix_infinity_norm(matrix):
    return max(sum(abs(value) for value in row) for row in matrix)

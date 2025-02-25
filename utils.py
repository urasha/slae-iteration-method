def check_diagonal_dominance(matrix):
    size = len(matrix)
    for row_index in range(size):
        sum_off_diagonal = sum(
            abs(matrix[row_index][col_index]) for col_index in range(size) if row_index != col_index
        )
        if abs(matrix[row_index][row_index]) < sum_off_diagonal:
            return False
    return True


def sort_for_diagonal_dominance(matrix):
    n = len(matrix)
    for i in range(n):
        max_row = max(range(i, n), key=lambda x: abs(matrix[x][i]))
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
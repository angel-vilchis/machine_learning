# Matrix-Matrix Multiplication (General)
def matrix_multiplication(matrix_a, matrix_b):
    matrix_a_rows = len(matrix_a)
    matrix_a_cols = len(matrix_a[0])
    matrix_b_rows = len(matrix_b)
    matrix_b_cols = len(matrix_b[0])

    if (matrix_a_cols != matrix_b_rows):
        return [[]]
    inner_dimension = matrix_a_cols

    matrix_c = [[0 for i in range(matrix_b_cols)] for j in range(matrix_a_rows)]

    for row_i in range(matrix_a_rows):
        for col_i in range(matrix_b_cols):
            for id_i in range(inner_dimension): 
                matrix_c[row_i][col_i] += matrix_a[row_i][id_i] * matrix_b[id_i][col_i]
    return matrix_c
  
# Matrix-Matrix Multiplication If Sparse (For Efficiency)
def sparse_matrix_multiplication(matrix_a, matrix_b):
    matrix_a_rows = len(matrix_a)
    matrix_a_cols = len(matrix_a[0])
    matrix_b_rows = len(matrix_b)
    matrix_b_cols = len(matrix_b[0])

    if (matrix_a_cols != matrix_b_rows):
        return [[]]
    inner_dimension = matrix_a_cols

    matrix_c = [[0 for i in range(matrix_b_cols)] for j in range(matrix_a_rows)]
    
    nonzero_entries_a = nonzero_entries(matrix_a)
    nonzero_entries_b = nonzero_entries(matrix_b)

    for row_i, inner_i in nonzero_entries_a.keys():
        for col_i in range(matrix_b_cols): 
            if (inner_i, col_i) in nonzero_entries_b.keys():
                matrix_c[row_i][col_i] += nonzero_entries_a[(row_i, inner_i)] * nonzero_entries_b[(inner_i, col_i)]
    return matrix_c

def nonzero_entries(matrix):
    nonzero_entries = {}
    for row_i in range(len(matrix)):
        for col_i in range(len(matrix[0])):
            if matrix[row_i][col_i] != 0:
                nonzero_entries[(row_i, col_i)] = matrix[row_i][col_i]
    return nonzero_entries

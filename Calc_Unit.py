import numpy as np

""" Calculation """

def Randomize_Matrix(val_range: int, size: int) -> np.ndarray:
    return np.random.randint(-val_range, val_range, size=(size, size))

def Format_Matrix(matrix) -> np.ndarray:
    matrix = np.array((matrix), dtype=float)
    shape_matrix = matrix.shape
    if shape_matrix[0] != shape_matrix[1]:
        raise Exception (f"Input matrix is not square: {shape_matrix}")
    return matrix

def Round_Complex(value: np.complex128) -> tuple:
    return (np.around(value.real, decimals=3), np.around(value.imag, decimals=3))

def Exact_Eigenvalues(matrix: np.ndarray) -> np.ndarray:
    eigenvalues = np.linalg.eig(matrix)[0]
    return [Round_Complex(x) for x in eigenvalues]

def Gerschgorin(matrix: np.ndarray) -> np.ndarray:
    eigenvalues = []
    for i in range(len(matrix)):
        sum_row = np.sum(np.abs(matrix[i])) - np.abs(matrix[i][i])
        eigenvalues.append((matrix[i][i], sum_row))
    return eigenvalues

def Circle_Theorem(matrix, calc_exact_ev: bool = True):
    if type(matrix) == list:
        matrix = Format_Matrix(matrix)
    
    gerschgorin_eigenvalues = Gerschgorin(matrix)

    if calc_exact_ev:
        exact_eigenvalues = Exact_Eigenvalues(matrix)
        return gerschgorin_eigenvalues, exact_eigenvalues
    
    return gerschgorin_eigenvalues


if __name__ == "__main__":
    test_matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
    test_matrix_2 = Randomize_Matrix(10, 4)

    test_matrix_1 = Circle_Theorem(test_matrix_1, False)
    test_matrix_2, exact_values = Circle_Theorem(test_matrix_2)






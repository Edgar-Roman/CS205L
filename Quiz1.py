import numpy as np
import sympy

MATRIX = np.asarray([[1, 0, 1],
                     [0, 1, 1],
                     [0, 0, 0]])

if __name__ == '__main__':
    columns = [list(MATRIX[:, i]) for i in range(len(MATRIX))]
    columnspace = sympy.Matrix(MATRIX).columnspace()
    s = ""
    for i in range(len(columnspace)):
        if list(columnspace[i]) in columns:
            if i == 0:
                s += "1st "
            elif i == 1:
                s += "2nd "
            else:
                s += "3rd "
    print("The {}column vector(s) span(s) the columnspace of the matrix".format(s))
    det = np.linalg.det(MATRIX)
    if det == 0:
        print("Singular!")
    else:
        print("Not Singular!")

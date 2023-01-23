import numpy as np

A = np.array([[10e-10, 0],
              [0, 10e10]])

if __name__ == '__main__':
    conditionNumber = np.linalg.cond(A)
    print("Condition Number = {}".format(conditionNumber))


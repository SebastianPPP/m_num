import numpy as np
import matplotlib as plt

#Metody iteracyjne [Gauss-Seidel]

def Gauss_Seidel(A, B):
    #elementy na głównej przekątnej nie mogą być zerowe
    #mamy macierz z num_eq wierszami i num_of_x niewiadomymi
    #zakładamy zerowy wektor początkowy x=[0 0 0 ...]^T
    num_of_rows = A.shape[0]
    X = np.zeros(num_of_rows)
    for j in range(5):
        for k in range(num_of_rows):
            sum = 0
            for l in range(num_of_rows):
                if l != k:
                    sum += A[k, l] * X[l]
            X[k] = (B[k]-sum)/A[k,k]
    return X.T

A = np.array([
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10]
])

B = np.array([7.85, -19.3, 71.4])
B1 = B.T

print(Gauss_Seidel(A,B1))

## Do zrobienia relaksacja
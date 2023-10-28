import numpy as np
import matplotlib as plt

#Metody iteracyjne [Gauss-Seidel]

def Gauss_Seidel(macierz_A, macierz_B):
    #elementy na głównej przekątnej nie mogą być zerowe
    #mamy macierz z num_eq wierszami i num_of_x niewiadomymi
    #zakładamy zerowy wektor początkowy x=[0 0 0 ...]^T



macierz_A = np.array([
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, 0.2, 10]
])
macierz_B = np.array([7.85, -19.3, 71.4])

print(macierz_A)
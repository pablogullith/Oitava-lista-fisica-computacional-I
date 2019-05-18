#Autor: Pablo gullith
#Bibliotecas
import numpy as np
import numpy.linalg as npl

def f(m, n):
    if m == n:
        return L/2
    else:
        return 0

def g(m, n): 
    if m == n:
        return (L**2)/4
    elif m%2 == n%2:
        return 0
    else:
        return -((2*L/np.pi)**2)*m*n/((m**2 - n**2)**2)

def H(m, n):
    A = (h**2)*(np.pi**2)*(n**2)/M/(L**3)
    B = 2*a/(L**2)
    
    return A*f(m, n) + B*g(m, n)

def matriz_H(N):
    A = np.empty([N, N], float)
    for m in range(N):
        for n in range(N):
            A[m, n] = H(m + 1, n + 1)
    return A

L = 5e-10 
h = 197.32697e-9 
a = 10 
M = 0.511e6 

print("Matriz 10X10:\n\n", npl.eigvalsh(matriz_H(10)), "\nMatriz 100X100:\n\n", npl.eigvalsh(matriz_H(100))[:10])

""" Alguns comentários: 
Quando fazemos novamente o calculo para 100x100 é pequeno o ganho de precisão em temperaturas baixas. É perceptivel
que quando os números quanticos crescem é viável aumentar a quantidade de termos do hemiltoniano para podermos calcular
os autovalores.""" 



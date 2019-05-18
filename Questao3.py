#Autor: Pablo Gullith
#Bibliotecas
from scipy import zeros, empty, dot, sqrt, array, copy, identity
from scipy import transpose

def Decomposicao_Auto(A,error):
    
    N = A.shape[0]

    def QR_Decomposicao(A):
        
        N = A.shape[0]
        Q = empty([N,N],float)
        R = zeros([N,N],float)

        A_Colunas = []
        for i in range(N):
            A_Colunas.append(A[:,i])

        def Vetor_Comprimento(v): 
            return sqrt(dot(v, v))

        u_Colunas = [ copy(A_Colunas[0]) ]
        q_Colunas = [ copy(A_Colunas[0]) / Vetor_Comprimento(A_Colunas[0]) ]
        for i in range(1, N):
            u_Colunas.append(copy(A_Colunas[i]))
            for j in range(i):
                u_Colunas[i] -= dot(q_Colunas[j], A_Colunas[i]) * q_Colunas[j]
            q_Colunas.append(u_Colunas[i] / Vetor_Comprimento(u_Colunas[i]))

        #Criar matriz Q
        for i in range(N):
            Q[:, i] = q_Colunas[i]

        #Criar matriz R
        for i in range(N):
            for j in range(i, N):
                if i == j:
                    R[i, i] = Vetor_Comprimento(u_Colunas[i])
                else:
                    R[i, j] = dot(q_Colunas[i], A_Colunas[j])

        return [ Q, R ]

    def A1(a): 
        def A2(x): 
            if abs(x) < error:
                return True
            else:
                return False

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                else:
                    if not A2(a[i, j]):
                        return False
        return True

    V = identity(N)
    while(not A1(A)):
       
        Q, R  = QR_Decomposicao(A)
        A = dot(R, Q)
        V = dot(V, Q)
    return [ V, A ]


A = array([ [1, 4, 8, 4],
            [4, 2, 3, 7],
            [8, 3, 6, 9],
            [4, 7, 9, 2] ],float)
[Auto_Vetores, Auto_Valores] = Decomposicao_Auto(A, 1e-6)

print('MATRIZ DOS AUTOVETORES:\n')
print(Auto_Vetores)
print('\nMATRIZ DOS AUTOVALORES:\n')
print(Auto_Valores)

#Alguns comentários:
#Perceba que a matriz dos autovalores retorna em sua diagonal principal os valores mostrados como resposta
#na lista
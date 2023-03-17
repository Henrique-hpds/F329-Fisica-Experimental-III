import pandas as pd
from ponto import *

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def ler_dados(pontos:list) -> None:
    dados = pd.read_excel("dados_inventados.xlsx")

    x = dados["x"]
    y = dados["y"]
    ddp = dados["ddp"]

    x = [int(i) for i in x]
    y = [int(i) for i in y]
    ddp = [float(i) for i in ddp]

    n_colunas = 0
    n_linhas = 0
    x_inicial = x[0]
    i = 0

    while x[i] == x_inicial:
        i+=1
    n_colunas = int(((len(x)/i) * 2)+ 3) 
    n_linhas = int((i * 2) + 3)
    
    matriz = [ [0 for i in range(n_linhas)] for j in range(n_colunas)]

    for i in range(len(x)):
        matriz[2 * x[i]][2 * y[i]] = ddp[i]
 
    for i in range(2, n_colunas - 2, 2):
        for j in range(2, n_linhas - 2, 2):
            if matriz[i + 2][j] != 0:
                matriz[i + 1][j] = (matriz[i][j] + matriz[i + 2][j])/2 
            
            if matriz[i - 2][j] != 0:
                matriz[i - 1][j] = (matriz[i][j] + matriz[i - 2][j])/2 

            if matriz[i][j + 2] != 0:
                matriz[i][j + 1] = (matriz[i][j] + matriz[i][j + 2])/2 

            if matriz[i][j - 2] != 0:
                matriz[i][j - 1] = (matriz[i][j] + matriz[i][j - 2])/2 

    for i in range(2, n_colunas - 2, 2):
        for j in range(3, n_linhas - 2, 2):
            if matriz[i + 2][j] != 0:
                matriz[i + 1][j] = (matriz[i][j] + matriz[i + 2][j])/2 
            
            if matriz[i - 2][j] != 0:
                matriz[i - 1][j] = (matriz[i][j] + matriz[i - 2][j])/2 

            if matriz[i][j + 2] != 0:
                matriz[i][j + 1] = (matriz[i][j] + matriz[i][j + 2])/2 

            if matriz[i][j - 2] != 0:
                matriz[i][j - 1] = (matriz[i][j] + matriz[i][j - 2])/2 

    x_ = []
    y_ = []
    ddp_= []

    k = 0
    for i in range(2, n_colunas - 2):
        for j in range(2, n_linhas - 2):
            ddp_.append(matriz[i][j])
            if i%2 == 0:
                x_.append(i/2)
            elif i%2 != 0:
                x_.append(float(i/2))

            if j%2 == 0:
                y_.append(j/2)
            elif j%2 != 0:
                y_.append(float(j/2))

    print(len(x_))

    for i in range(len(x_)):
        pontos.append(Ponto(x_[i], y_[i], ddp_[i]))


# for i in range(2, n_colunas - 2, 1):
#     for j in range(2, n_linhas - 2, 1):
#         if matriz[i][j] == 0:
#             print("------", end="\t")
#             # print("0.0000", end="\t")
#         else:
#             print(truncate(matriz[i][j], 4), end="\t")
#     print()
#     print()
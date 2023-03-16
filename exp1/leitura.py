import pandas as pd
from ponto import *

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
                matriz[i - 2][j] = (matriz[i][j] + matriz[i - 2][j])/2 

            if matriz[i][j + 2] != 0:
                matriz[i][j + 1] = (matriz[i][j] + matriz[i][j + 2])/2 

            if matriz[i][j - 2] != 0:
                matriz[i][j - 1] = (matriz[i][j] + matriz[i][j - 2])/2 

    x_ = []
    y_ = []
    ddp_= []
    # for _ in range(len(y) * 2 - 1):
    #     x.append(None)
    #     y.append(None)
    #     ddp.append(None)
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

    for i in range(len(x_)):
        pontos.append(Ponto(x_[i], y_[i], ddp_[i]))


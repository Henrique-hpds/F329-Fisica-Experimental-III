import pandas as pd
from ponto import *

def ler_dados(pontos:list) -> None:
    dados = pd.read_excel("dados_inventados.xlsx")

    coluna_x = dados["x"]
    coluna_y = dados["y"]
    coluna_ddp = dados["ddp"]

    coluna_x_completa = list()
    coluna_y_completa = list()
    coluna_ddp_completa = list()
    
    coluna_x_completa.append(float(coluna_x[0]))
    coluna_y_completa.append(float(coluna_y[0]))
    coluna_ddp_completa.append(float(coluna_ddp[0]))

    for i in range(len(coluna_x) - 1):
        if coluna_x[i] == coluna_x[i+1]:
            if not (coluna_x_completa[-1] == coluna_x[i] and coluna_y_completa[-1] == coluna_y[i]):
                coluna_x_completa.append(float(coluna_x[i])) 
                coluna_y_completa.append(float(coluna_y[i]))
                coluna_ddp_completa.append(float(coluna_ddp[i]))

            coluna_x_completa.append(float(coluna_x[i]))
            coluna_y_completa.append((float(coluna_y[i]) + float(coluna_y[i+1]))/2)
            coluna_ddp_completa.append((float(coluna_ddp[i]) + float(coluna_ddp[i+1]))/2)

            coluna_x_completa.append(float(coluna_x[i + 1]))
            coluna_y_completa.append(float(coluna_y[i + 1]))
            coluna_ddp_completa.append(float(coluna_ddp[i + 1]))



    for i in range(len(dados)):
        pontos.append(Ponto(coluna_x_completa[i], coluna_y_completa[i], coluna_ddp_completa[i]))
    
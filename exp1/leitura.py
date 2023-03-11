import pandas as pd
from ponto import *

def ler_dados(pontos:list) -> None:
    dados = pd.read_excel("dados_inventados.xlsx")

    coluna_x = dados["x"]
    coluna_y = dados["y"]
    coluna_ddp = dados["ddp"]

    for i in range(len(dados)):
        pontos.append(Ponto(float(coluna_x[i]), float(coluna_y[i]), float(coluna_ddp[i])))
    
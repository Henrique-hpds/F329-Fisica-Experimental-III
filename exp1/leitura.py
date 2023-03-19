import pandas as pd
from ponto import *
from interpolador import interpolar

def ler_dados(pontos:list) -> None:
    dados = pd.read_excel("ceu.xlsx")

    x = dados["x"]
    y = dados["y"]
    ddp = dados["ddp"]

    x = [int(i) for i in x]
    y = [int(i) for i in y]
    ddp = [float(i) for i in ddp]

    interpolar(x, y, ddp)

    for i in range(len(x)):
        pontos.append(Ponto(x[i], y[i], ddp[i]))
import matplotlib.pyplot as plt
import pandas as pd
from ponto import Ponto

def ler_dados(pontos):
    dados = pd.read_excel("dados_inventados.xlsx")

    coluna_x = dados["x"]
    coluna_y = dados["y"]
    coluna_ddp = dados["ddp"]

    for i in range(len(coluna_x)):
        pontos.append(Ponto(int(coluna_x[i]), int(coluna_y[i]), float(coluna_ddp[i])))
    

def printar_pontos(pontos):
    for i in range(len(pontos)):
        pontos[i].printar()


def main():
    pontos = list()
    
    ler_dados(pontos)
    printar_pontos(pontos)

if __name__ == "__main__":
    main()
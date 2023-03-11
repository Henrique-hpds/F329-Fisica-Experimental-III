import matplotlib.pyplot as plt
import pandas as pd
from ponto import Ponto

def ler_dados(pontos:list) -> None:
    dados = pd.read_excel("dados_inventados.xlsx")

    coluna_x = dados["x"]
    coluna_y = dados["y"]
    coluna_ddp = dados["ddp"]

    for i in range(len(dados)):
        pontos.append(Ponto(int(coluna_x[i]), int(coluna_y[i]), float(coluna_ddp[i])))
    

def printar_pontos(pontos:list) -> None:
    for atual in pontos:
        atual.printar()
        
        
def main():
    pontos = list()
    
    ler_dados(pontos)
    
    pontos = sorted(pontos, key=lambda ponto: ponto.ddp)
    printar_pontos(pontos)


if __name__ == "__main__":
    main()
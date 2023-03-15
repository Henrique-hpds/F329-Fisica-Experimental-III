import matplotlib.pyplot as plt
import random as rd

ERRO = 0.05
    
def plota_grafico(pontos: list) -> None:
    
    
    plt.xlabel("Eixo x (cm)")
    plt.ylabel("Eixo y (cm)")
    plt.title("Curvas de Nível de Tensão")
    
    coluna_x = list()
    coluna_y = list()
    
    menor = pontos[0].ddp
    
    for atual in pontos:
        if atual.ddp - menor <= ERRO:
            coluna_x.append(atual.coordenada["x"])
            coluna_y.append(atual.coordenada["y"])
        else:
            plt.scatter(coluna_x, coluna_y, label=str((menor + ERRO)/2) + ' V ± ' + str(ERRO/2)) # markeredgecolor=cor , markerfacecolor="black", markersize=2,marker="o"
            menor = atual.ddp
 
            coluna_x.clear()
            coluna_y.clear()
            coluna_x.append(atual.coordenada["x"])
            coluna_y.append(atual.coordenada["y"])            
    
    plt.legend()
    plt.show()
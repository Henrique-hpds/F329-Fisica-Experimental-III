import matplotlib.pyplot as plt
import random as rd

ERRO = 0.08

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

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
            plt.scatter(coluna_x, coluna_y, label=truncate((menor + ERRO)/2, 2) + ' V ± ' + truncate(ERRO/2, 2)) # markeredgecolor=cor , markerfacecolor="black", markersize=2,marker="o"
            menor = atual.ddp
 
            coluna_x.clear()
            coluna_y.clear()
            coluna_x.append(atual.coordenada["x"])
            coluna_y.append(atual.coordenada["y"])            
    
    plt.legend()
    plt.show()
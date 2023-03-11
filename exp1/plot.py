import matplotlib.pyplot as plt
import random as rd

ERRO = 0.05

lista_cores = ['#5465FF', '#45F0DF', '#D0C4DF', '#157145', '#111D4A', '#FFBA08', '#D00000', '#6EEB83', '#B8336A']

rd.seed()

def cor_random():
    rand = rd.randint(0, len(lista_cores) - 1)
    cor = lista_cores[rand]
    lista_cores.pop(rand)
    return cor
    
def plota_grafico(pontos: list) -> None:
    
    
    plt.xlabel("Eixo x (cm)")
    plt.ylabel("Eixo y (cm)")
    plt.title("Curvas de Nível de Tensão")
       
    # pontos_plot = list()
    # lista_menores = list()
    # lista_cores_usadas = list()
    
    coluna_x = list()
    coluna_y = list()
    
    menor = pontos[0].ddp
    
    for atual in pontos:
        if atual.ddp - menor <= ERRO:
            # pontos_plot.append(atual)
            coluna_x.append(atual.coordenada["x"])
            coluna_y.append(atual.coordenada["y"])
        else:
            # lista_menores.append(menor)
            cor = cor_random()
            plt.scatter(coluna_x, coluna_y, label=str(menor) + ' V') # markeredgecolor=cor , markerfacecolor="black", markersize=2,marker="o"
            menor = atual.ddp
            # for i in pontos_plot:
                # plt.plot(i.coordenada["x"], i.coordenada["y"], markeredgecolor=cor , markerfacecolor="black", markersize=2,marker="o")
                # plt.scatter()
            # pontos_plot.clear()
            # pontos_plot.append(atual)
            coluna_x.clear()
            coluna_y.clear()
            coluna_x.append(atual.coordenada["x"])
            coluna_y.append(atual.coordenada["y"])            
            
            
            
    
    # for i in range(len(lista_menores)):
    #     lista_menores[i] = str(lista_menores[i]) + ' V'
        
    
    plt.legend()
    plt.show()
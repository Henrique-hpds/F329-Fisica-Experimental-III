from ponto import *
from leitura import *
from plot import *
        
def main():
    pontos = list()
    
    ler_dados(pontos)
    
    pontos = sorted(pontos, key=lambda ponto: ponto.ddp)
    
    plota_grafico(pontos)

if __name__ == "__main__":
    main()
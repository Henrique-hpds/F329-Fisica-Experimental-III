import matplotlib.pyplot as plt
import pandas as pd
from ponto import Ponto

pontos = list()

dados = pd.read_excel("dados_inventados.xlsx")

# print(dados)

for atual in dados:
    pontos.append(Ponto(atual["x"], atual["y"], atual["ddp"]))
    print(atual)

# coluna_x = pd.read_excel("dados_inventados.xlsx", "x")
# print(coluna_x[1])
# coluna_y = list()
# coluns_ddp = list()



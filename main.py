# %%
import pandas as pd

# Ajustes de exibição
pd.set_option('display.max_rows', None)   # mostra todas as linhas
pd.set_option('display.max_columns', None)  # mostra todas as colunas
pd.set_option('display.width', None)     # evita quebra de linha
pd.set_option('display.max_colwidth', None)  # mostra o conteúdo inteiro da célula

# Carregar e exibir
tabela = pd.read_excel("bigData.xlsx")
tabela
# %%

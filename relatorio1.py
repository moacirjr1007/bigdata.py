from IPython.display import display
import pandas as pd

tabela = pd.read_csv("bigData.csv", nrows=500000, sep=';')
display(tabela)
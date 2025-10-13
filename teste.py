import pandas as pd

# Ajustes de exibição
pd.set_option("display.max_rows", None)   
pd.set_option("display.max_columns", None) 
pd.set_option("display.expand_frame_repr", None)
pd.set_option("display.width", None)     
#pd.set_option('display.max_colwidth', None)  

abas = pd.read_excel("bigData.xlsx", sheet_name=None)

#print(abas.keys())

df_aba1 = abas["RELATORIO 2022"]
df_aba2 = abas["RELATORIO 2023"]
df_aba3 = abas["RELATORIO 2024"]
df_aba4 = abas["RELATORIO 2025"]

#print(df_aba1, df_aba2, df_aba3, df_aba4)

df_completo = pd.concat(abas.values(), ignore_index=True)

#print(df_completo)

#numero_itens = len("bigData.xlsx")

print(df_completo[["Funcionário", "Função", "Data do Exame", "Responsável ASO"]])
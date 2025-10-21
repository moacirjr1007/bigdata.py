# Importa a biblioteca pandas, essencial para análise de dados
# Importa a função 'show' da nova biblioteca de GUI
import pandas as pd
from pandasgui import show

# Lê o ficheiro Excel e carrega TODAS as abas de uma vez (sheet_name=None)
# 'abas' torna-se um dicionário (uma coleção de tabelas).
abas = pd.read_excel("bigData.xlsx", sheet_name=None)


# Junta (concatena) todas as tabelas guardadas em 'abas.values()'
# numa única tabela chamada 'df_completo'.
df_completo = pd.concat(abas.values(), ignore_index=True)

# Limpa os dados e guardar numa nova variável
df_final = df_completo.dropna(subset=["Funcionário", "Data do Exame"])

# Selecionamos apenas as colunas que queremos ver
# show() abre uma nova janela com a tabela exigida 
df_exibicao = df_final[["Funcionário", "Data do Exame"]]
show(df_exibicao)
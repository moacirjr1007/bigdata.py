import pandas as pd
from pandasgui import show

# Lê o ficheiro Excel e carrega TODAS as abas de uma vez (sheet_name=None)
# 'abas' torna-se um dicionário (uma coleção de tabelas).
abas = pd.read_excel("bigData.xlsx", sheet_name=None)


# Junta (concatena) todas as tabelas guardadas em 'abas.values()'
# numa única tabela chamada 'relatorio_completo'.
relatorio_completo = pd.concat(abas.values(), ignore_index=True)

# Limpa os dados e guardar numa nova variável
relatorio_final = relatorio_completo.dropna()

# show() abre uma nova janela com a tabela exigida 
show(relatorio_final)
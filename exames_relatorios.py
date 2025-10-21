import pandas as pd

# Ajustes de exibição (verifique se não há caracteres estranhos aqui!)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", None)
pd.set_option("display.width", None)
pd.set_option('display.max_colwidth', None)

# Carregamento dos dados
abas = pd.read_excel("bigData.xlsx", sheet_name=None)
df_completo = pd.concat(abas.values(), ignore_index=True)

# -----------------------------------------------------------
# ETAPA DE LIMPEZA DE DADOS
# -----------------------------------------------------------

# Converte a data e elimina linhas vazias, conforme discutido anteriormente
df_completo.dropna(how='all', inplace=True)
df_completo.dropna(subset=['Exames', 'Data do Exame'], inplace=True)

# Lembre-se de adicionar dayfirst=True para evitar warnings
df_completo['Data do Exame'] = pd.to_datetime(
    df_completo['Data do Exame'], 
    errors='coerce',
    dayfirst=True 
)


print(df_completo[["Exames", "Data do Exame"]])
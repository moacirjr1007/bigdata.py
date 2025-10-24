import pandas as pd
import matplotlib.pyplot as plt # Biblioteca para gráficos estatísticos
import seaborn as sns # Biblioteca para gráficos estatísticos

# Ajustes de exibição (mantidos)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", None)
pd.set_option("display.width", None)
pd.set_option('display.max_colwidth', None)

# Carregamento dos dados
abas = pd.read_excel("bigData.xlsx", sheet_name=None)
df_completo = pd.concat(abas.values(), ignore_index=True)

# -----------------------------------------------------------
# PREPARAÇÃO DOS DADOS PARA O GRÁFICO
# -----------------------------------------------------------

# 1. Converte a coluna 'Data do Exame' para datetime
df_completo['Data do Exame'] = pd.to_datetime(df_completo['Data do Exame'], errors='coerce')

# 2. Cria a coluna 'Ano'
df_completo['Ano'] = df_completo['Data do Exame'].dt.year

# 3. Identifica os 10 exames mais frequentes (para evitar um gráfico poluído)
# Se você tiver apenas alguns exames diferentes, remova o .head(10)
top_10_exames = df_completo['Exames'].value_counts().head(10).index.tolist()

# 4. Filtra o DataFrame para incluir apenas os Top 10 Exames
df_top_exames = df_completo[df_completo['Exames'].isin(top_10_exames)]

# 5. Agrupa e conta a frequência de cada exame por ano (Data Wrangling)
# Esta tabela cruzada é a base para o nosso gráfico
df_frequencia = df_top_exames.groupby(['Ano', 'Exames']).size().reset_index(name='Contagem')

# -----------------------------------------------------------
# PLOTAGEM DO GRÁFICO DE BARRAS AGRUPADAS (SEABORN)
# -----------------------------------------------------------

plt.figure(figsize=(14, 8)) # Aumenta o tamanho da figura para melhor visualização

# Cria o Gráfico de Barras Agrupadas
# X = Anos, Y = Contagem, Hue = O tipo de Exame
sns.barplot(
    data=df_frequencia,
    x='Ano',
    y='Contagem',
    hue='Exames',
    palette='Spectral' # Escolhe uma paleta de cores para os exames
)

plt.title('Contagem dos Top 10 Exames Realizados por Ano', fontsize=16)
plt.xlabel('Ano do Exame', fontsize=12)
plt.ylabel('Total de Exames Realizados', fontsize=12)

# Coloca a legenda fora da área de plotagem para não atrapalhar
plt.legend(title='Tipo de Exame', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.grid(axis='y', linestyle='--', alpha=0.7) # Adiciona linhas de grade no eixo Y

# Ajusta o layout e exibe o gráfico
plt.tight_layout(rect=[0, 0, 0.9, 1]) # Ajusta para acomodar a legenda
plt.show()
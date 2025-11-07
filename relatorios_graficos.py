# Bibliotecas utilizadas:
import pandas as pd # Biblioteca para manipular arquivos excell
import matplotlib.pyplot as plt # Biblioteca para gerar gráficos e estilizar
import io # Usado para criar "arquivos falsos" na memória RAM
import base64 # Importante: Usado para converter imagens em texto
import numpy as np # Gera a sequência de números (np.linspace) para criar o degradê de cores dos gráficos.


# Define o nome do arquivo Excel que vamos ler.
arquivo_excel = "bigData.xlsx"


def gerar_relatorio_completo():
    """Lê, junta e limpa todos os dados."""
    
    # Caso dê tudo certo ele irá rodar o try:
    try:
        # abas = Lê TODAS as abas do Excel.
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        # relatorio_completo = Junta (Concatena) todas as abas em um único relatório.
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)
        # relatorio_final = Limpa o relatório, retirando as partes em branco (NaN).
        relatorio_final = relatorio_completo.dropna()
        
        # A MUDANÇA: Em vez de salvar, nós 'return' (retornamos) a tabela
        # (o DataFrame) pronta para o 'app.py'.
        return relatorio_final
        
    # Caso dê errado ele irá rodar o except:
    except Exception as e:
        # print = Exibe a mensagem de erro no terminal.
        print(f"Erro ao gerar relatório completo: {e}")
        # return = Retorna 'None' (vazio) para o 'app.py' saber que falhou.
        return None

def gerar_relatorio_funcionarios():
    """Filtra o relatório por Funcionário e Data do Exame."""
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)
        
        # relatorio_final = Limpa o relatório, focando nas colunas específicas.
        relatorio_final = relatorio_completo.dropna(subset=["Funcionário", "Data do Exame"])
        # relatorio_exibicao = Define as colunas que iremos exibir.
        relatorio_exibicao = relatorio_final[["Funcionário", "Data do Exame"]]

        # A MUDANÇA: Retorna a tabela (DataFrame) filtrada.
        return relatorio_exibicao
        
    except Exception as e:
        print(f"Erro ao gerar relatório de funcionários: {e}")
        return None

def gerar_relatorio_exames():
    """Filtra o relatório por Exames e Data do Exame."""
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)

        relatorio_final = relatorio_completo.dropna(subset=["Exames", "Data do Exame"])
        relatorio_exibicao = relatorio_final[["Exames", "Data do Exame"]]

        # A MUDANÇA: Retorna a tabela (DataFrame) filtrada.
        return relatorio_exibicao
        
    except Exception as e:
        print(f"Erro ao gerar relatório de exames: {e}")
        return None
        
def gerar_relatorio_funcao():
    """Filtra o relatório por Função e Data do Exame."""
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)

        relatorio_final = relatorio_completo.dropna(subset=["Função", "Data do Exame"])
        relatorio_exibicao = relatorio_final[["Função", "Data do Exame"]]

        # A MUDANÇA: Retorna a tabela (DataFrame) filtrada.
        return relatorio_exibicao
        
    except Exception as e:
        print(f"Erro ao gerar relatório de função: {e}")
        return None

# --- Funções de Gráfico (AGORA RETORNAM TEXTO Base64) ---

def gerar_graficos_funcionarios():
    """Gera um gráfico Top 10 Funcionários e retorna como string Base64."""
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        dados_completos = pd.concat(abas.values(), ignore_index=True)
        
        # (Toda a sua lógica de filtrar os dados e contar os valores)
        dados_filtrados = dados_completos[
            dados_completos['Funcionário'].notna() & 
            (dados_completos['Funcionário'].astype(str).str.strip() != '') &
            (~dados_completos['Funcionário'].astype(str).str.lower().isin(['funcionário', 'funcionario', '']))
        ]
        exames_por_funcionario = dados_filtrados['Funcionário'].value_counts().head(10)
        
        # (Toda a sua lógica de criar o gráfico com Matplotlib)
        fig, ax = plt.subplots(figsize=(12, 5))
        cores = plt.cm.Greens(np.linspace(0.4, 0.9, len(exames_por_funcionario)))
        bars = ax.barh(exames_por_funcionario.index, exames_por_funcionario.values,
                       color=cores, height=0.7, edgecolor='white', linewidth=1)
        ax.set_title('TOP 10 FUNCIONÁRIOS - MAIS EXAMES REALIZADOS\n (2022-2025)', fontsize=12, fontweight='bold', pad=10)
        ax.invert_yaxis()
        # (etc...)
        plt.tight_layout() 

        # --- A MUDANÇA: Converter o gráfico para Texto (Base64) ---
        
        # img_buffer = Cria um "arquivo falso" na memória RAM.
        img_buffer = io.BytesIO()
        
        # fig.savefig = Salva a figura (fig) nesse arquivo da memória (em formato PNG).
        fig.savefig(img_buffer, format="png", bbox_inches="tight", dpi=100)
        # plt.close = Fecha o gráfico da memória para não vazar.
        plt.close(fig)
        # img_buffer.seek(0) = "Rebobina" o arquivo da memória para o início.
        img_buffer.seek(0)
        
        # string_base64 = Converte a imagem (PNG) em um texto longo (Base64).
        string_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        
        # return = Retorna o TEXTO do gráfico para o 'app.py'.
        return string_base64
    
    except Exception as e:
        print(f"Erro ao gerar gráfico de funcionários: {e}")
        return None

def gerar_graficos_exames():
    """Gera um gráfico Top 10 Exames e retorna como string Base64."""
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        dados_completos = pd.concat(abas.values(), ignore_index=True)

        # (Toda a sua lógica de criar o gráfico)
        plt.figure(figsize=(12, 5))
        top_exames = dados_completos['Exames'].value_counts().head(10) 
        plt.barh(top_exames.index, top_exames.values, color=plt.cm.plasma(range(10))) 
        plt.title(f'TOP 10 EXAMES REALIZADOS\n (2022-2025)')
        plt.xlabel('Quantidade de Exames')
        plt.gca().invert_yaxis() 
        plt.tight_layout() 
        grafico_completo = plt.gcf()

        # --- A MUDANÇA: Converter o gráfico para Texto (Base64) ---
        img_buffer = io.BytesIO()
        grafico_completo.savefig(img_buffer, format="png", bbox_inches="tight")
        plt.close(grafico_completo)
        img_buffer.seek(0)
        
        string_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        return string_base64
    
    except Exception as e:
        print(f"Erro ao gerar gráfico de exames: {e}")
        return None

def gerar_graficos_funcao():
    """Gera um gráfico Top 15 Funções e retorna como string Base64."""
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        dados = pd.concat(abas.values(), ignore_index=True)
        
        top_funcoes = dados['Função'].value_counts().head(15)
        
        # (Toda a sua lógica de criar o gráfico)
        plt.figure(figsize=(12, 6))
        plt.barh(top_funcoes.index, top_funcoes.values, color=plt.cm.viridis(range(15)))
        plt.title(f'TOP 15 FUNÇÕES\n (2022-2025)')
        plt.gca().invert_yaxis()
        
        # --- A MUDANÇA: Converter o gráfico para Texto (Base64) ---
        img_buffer = io.BytesIO()
        # (plt.savefig salva a figura "ativa" no buffer)
        plt.savefig(img_buffer, format="png", bbox_inches="tight")
        plt.close() # Fecha a figura ativa
        img_buffer.seek(0)
        
        string_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        return string_base64
        
    except Exception as e:
        print(f"Erro: {e}")
        return None
# Biblietacas utilizadas:

import pandas as pd # Especialista em ler e munipular tabelas.
import matplotlib.pyplot as plt # Utilizado para gerar gráficos.
import io # Salva dados (como imagens de gráficos) na memória.
import os # O 'os' (Sistema Operacional) nos deixa interagir com arquivos e pastas.

from openpyxl import Workbook, drawing  
# É uma ferramenta extra para trabalhar com arquivos Excel (como adicionar gráficos).

arquivo_excel = "bigData.xlsx"
# Define o nome do arquivo Excel que vamos ler.

# Funções para gerar um relatório completo, utilizando o try e o excepect, logo abaixo:
# Observação: As funções de relatórios são praticamentes as mesmas, muda somente na parte de seleção
# de colunas de cada uma e na exibição.
def gerar_relatorio_completo():

    # Caso dê tudo certo ele irá rodar o try:

    # abas = Lê TODAS as abas do Excel de uma vez.
    # relatorio_completo = Junta (Concatena) todas as abas em um único relatório.
    # relatorio final = Limpa o relatório, retirando as partes em branco (NaN).
    # nome_arquivo_saida = Define o nome do novo arquivo Excel.
    # relatorio_final.to_excel() = Salva o relatório limpo nesse novo arquivo).
    # os.startfile() = Ao gerar o arquivo, ele o abre automaticamente.
    # return = Retorna o nome do arquivo para o app (Flask) enviar ao usuário. 

    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)
        
        relatorio_final = relatorio_completo.dropna() 

        nome_arquivo_saida = "Relatorio_Completo.xlsx"
        relatorio_final.to_excel(nome_arquivo_saida, index=False)

        os.startfile(nome_arquivo_saida) 

        return nome_arquivo_saida
    
    # Caso dê errado ele irá rodar o except:

    # print = Exibe a mensagem de erro ao gerar relatório no terminal.
    # return = Retorna vazio para o app (Flask).

    except Exception as e:
        print(f"Erro ao gerar relatório completo: {e}")
        return None
        
def gerar_relatorio_funcionarios():
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)
        
        relatorio_final = relatorio_completo.dropna(subset=["Funcionário", "Data do Exame"])
        # relatorio final = Limpa o relatório, retirando as partes em branco (NaN),
        # aqui também selecionamos a coluna que queremos que limpe no relatório.

        relatorio_exibicao = relatorio_final[["Funcionário", "Data do Exame"]]
        # relatorio_exibicao = Definimos as colunas limpas, que iremos exibir no relatório.

        nome_arquivo_saida = "Relatorio_Funcionarios.xlsx" 

        relatorio_exibicao.to_excel(nome_arquivo_saida, index=False)

        os.startfile(nome_arquivo_saida) 

        return nome_arquivo_saida
    except Exception as e:

        print(f"Erro ao gerar relatório de funcionários: {e}")
        return None

def gerar_relatorio_exames():
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)

        relatorio_final = relatorio_completo.dropna(subset=["Exames", "Data do Exame"])

        relatorio_exibicao = relatorio_final[["Exames", "Data do Exame"]]

        nome_arquivo_saida = "Relatorio_Exames.xlsx"

        relatorio_exibicao.to_excel(nome_arquivo_saida, index = False)

        os.startfile(nome_arquivo_saida) 

        return nome_arquivo_saida
    except Exception as e:

        print(f"Erro ao gerar relatório de exames: {e}")
        return None
    
def gerar_relatorio_funcao():
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)

        relatorio_final = relatorio_completo.dropna(subset=["Função", "Data do Exame"])

        relatorio_exibicao = relatorio_final[["Função", "Data do Exame"]]

        nome_arquivo_saida = "Relatorio_Funcao.xlsx"

        relatorio_exibicao.to_excel(nome_arquivo_saida, index = False)

        os.startfile(nome_arquivo_saida) 

        return nome_arquivo_saida
    except Exception as e:

        print(f"Erro ao gerar relatório de função: {e}")
        return None
    
def gerar_graficos_funcao():
    
    try:
        # Dados
        abas = pd.read_excel("bigData.xlsx", sheet_name=None)
        dados_completos = pd.concat(abas.values(), ignore_index=True)

        # Gráfico
        plt.figure(figsize=(12, 6))
        top_funcoes = dados_completos['Função'].value_counts().head(15)
        plt.barh(top_funcoes.index, top_funcoes.values, color=plt.cm.viridis(range(15)))
        plt.title(f'TOP 15 FUNÇÕES\n{len(dados_completos):,} registros (2022-2025)')
        plt.gca().invert_yaxis()

        grafico_completo = plt.gcf()

        # Excel
        wb = Workbook()
        img = io.BytesIO()

        grafico_completo.savefig(img, format="png", bbox_inches="tight")
        wb.active.add_image(drawing.image.Image(img), 'A1')

        nome_arquivo_saida = "Grafico_Funcao.xlsx"
        wb.save(nome_arquivo_saida)

        os.startfile(nome_arquivo_saida)
        
        return nome_arquivo_saida
    except Exception as e:

        print(f"Erro ao gerar gráfico de função: {e}")
        return None
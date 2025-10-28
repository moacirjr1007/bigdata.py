import pandas as pd, matplotlib.pyplot as plt, io, os
from openpyxl import Workbook, drawing


arquivo_excel = "bigData.xlsx"

def gerar_relatorio_completo():
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)
        
        relatorio_final = relatorio_completo.dropna() 

        nome_arquivo_saida = "Relatorio_Completo.xlsx"
        relatorio_final.to_excel(nome_arquivo_saida, index=False)

        os.startfile(nome_arquivo_saida) 

        return nome_arquivo_saida
    except Exception as e:
        print(f"Erro ao gerar relatório completo: {e}")
        return None
        
def gerar_relatorio_funcionarios():
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)
        
        relatorio_final = relatorio_completo.dropna(subset=["Funcionário", "Data do Exame"])

        relatorio_exibicao = relatorio_final[["Funcionário", "Data do Exame"]]

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

        print(f"Erro ao gerar relatório de exames: {e}")
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
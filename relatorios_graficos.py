import pandas as pd

arquivo_excel = "bigData.xlsx"

def gerar_relatorio_completo():
    try:
        abas = pd.read_excel(arquivo_excel, sheet_name=None)
        relatorio_completo = pd.concat(abas.values(), ignore_index=True)
        
        relatorio_final = relatorio_completo.dropna() 

        nome_arquivo_saida = "Relatorio_Completo.xlsx"
        relatorio_final.to_excel(nome_arquivo_saida, index=False)

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

        return nome_arquivo_saida
    except Exception as e:

        print(f"Erro ao gerar relatório de funcionários: {e}")
        return None

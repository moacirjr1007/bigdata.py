# Importamos o Flask e suas ferramentas.
# Note que NÃO usamos mais 'send_file', pois não vamos mais baixar arquivos.
from flask import Flask, render_template, request, redirect, url_for
import relatorios_graficos # Importamos nosso arquivo que faz o trabalho pesado.

# app = Cria a nossa aplicação web Flask. É o nosso servidor.
app = Flask(__name__)

# @app.route("/") = Define o que acontece quando alguém acessa o site principal.
@app.route("/")
def index():
    # return render_template = "Desenha" a tela 'principal.html' para o usuário.
    return render_template("principal.html")


# @app.route("/gerar") = Define o que acontece ao clicar no botão "Gerar".
@app.route("/gerar", methods=["POST"])
def gerar_relatorio():
    
    # if request.method = Confirma se os dados vieram do formulário (POST).
    if request.method == "POST":
        
        # escolha = Pega o "value" da opção que o usuário escolheu (ex: "relatorio_funcionarios").
        escolha = request.form["relatorio_escolhido"]

        # --- Variáveis que vamos "injetar" na nova tela (resultados.html) ---
        
        # titulo_pagina = Cria uma variável vazia para o título da nova tela.
        titulo_pagina = ""
        # relatorio_html = Cria uma variável vazia para guardar a TABELA.
        relatorio_html = None
        # grafico_base64 = Cria uma variável vazia para guardar a IMAGEM do gráfico.
        grafico_base64 = None

        
        # --- O Bloco de Decisão (O que fazer com a 'escolha') ---
        
        # Se a escolha for um RELATÓRIO:
        if escolha == "relatorio_completo":
            # titulo_pagina = Define o título que aparecerá na nova tela.
            titulo_pagina = "Relatório Completo"
            # df = Chama a função (do outro arquivo) que agora retorna uma tabela (DataFrame).
            df = relatorios_graficos.gerar_relatorio_completo()
            if df is not None:
                # A MUDANÇA: Converte a tabela (DataFrame) em um texto HTML.
                # Damos a ele a classe "tabela-estilizada" (do nosso CSS).
                relatorio_html = df.to_html(classes="tabela-estilizada", index=False)

        elif escolha == "relatorio_funcionarios":
            titulo_pagina = "Relatório de Funcionários"
            df = relatorios_graficos.gerar_relatorio_funcionarios()
            if df is not None:
                relatorio_html = df.to_html(classes="tabela-estilizada", index=False)

        elif escolha == "relatorio_exames":
            titulo_pagina = "Relatório de Exames"
            df = relatorios_graficos.gerar_relatorio_exames()
            if df is not None:
                relatorio_html = df.to_html(classes="tabela-estilizada", index=False)

        elif escolha == "relatorio_funcao":
            titulo_pagina = "Relatório por Função"
            df = relatorios_graficos.gerar_relatorio_funcao()
            if df is not None:
                relatorio_html = df.to_html(classes="tabela-estilizada", index=False)
        
        # Se a escolha for um GRÁFICO:
        elif escolha == "grafico_funcionarios":
            titulo_pagina = "Gráfico por Funcionários (TOP 10)"
            # A MUDANÇA: Chama a função que agora retorna um TEXTO (Base64) da imagem.
            grafico_base64 = relatorios_graficos.gerar_graficos_funcionarios()
            
        elif escolha == "grafico_exames":
            titulo_pagina = "Gráfico por Exames (TOP 10)"
            grafico_base64 = relatorios_graficos.gerar_graficos_exames()
            
        elif escolha == "grafico_funcao":
            titulo_pagina = "Gráfico por Função (TOP 15)"
            grafico_base64 = relatorios_graficos.gerar_graficos_funcao()

        
        # --- A Resposta para o Usuário ---

        # if ... is None = Se NADA foi gerado (ou seja, deu erro e a função retornou None)...
        if relatorio_html is None and grafico_base64 is None:
            # ...manda o usuário de volta para a página inicial.
            print(f"A função para '{escolha}' retornou None (provavelmente um erro).")
            return redirect(url_for("index"))

        # --- A MUDANÇA PRINCIPAL! ---
        
        # return render_template = Em vez de 'send_file' (baixar), 
        # nós vamos "desenhar" a nova página 'resultados.html'.
        # E "injetamos" nossas variáveis Python (titulo, relatorio_html, etc.)
        # dentro dos placeholders ({{...}}) do HTML.
        return render_template(
            "resultados.html", 
            titulo=titulo_pagina,
            relatorio_html=relatorio_html,
            grafico_base64=grafico_base64
        )

    # Se o método não for POST, volta para o início.
    return redirect(url_for("index"))


# Este é o comando que "liga" o servidor.
# 'debug=True' reinicia o servidor automaticamente quando salvamos o arquivo.
if __name__ == "__main__":
    app.run(debug=True)
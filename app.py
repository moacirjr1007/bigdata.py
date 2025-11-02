# Bibliotecas utilizadas:

# Importamos o Flask, onde vai ser o responsável pela a organização de rotas
from flask import Flask, render_template, request, send_file, redirect, url_for
import os # Importamos o os que interage com o sistema operacional.
import relatorios_graficos # Importamos nosso OUTRO arquivo Python, onde está a lógica dos relatórios.

# Aqui, criamos a  aplicação web Flask. A variável 'app' é o nosso servidor.
app = Flask(__name__)

# Define o que acontece quando alguém acessa a página principal (o "/").
# O Flask procura este arquivo na pasta "templates" por padrão.
@app.route("/")
def index():
    return render_template("principal.html")


# Define o que acontece quando o botão "Gerar" é clicado.
# Ele "ouve" a URL "/gerar" e só aceita o método "POST" (envio de formulário).
@app.route("/gerar", methods=["POST"])
def gerar_relatorio():
    
    # Confirma se os dados estão vindo de um formulário (POST).
    if request.method == "POST":
        # Pega o "value" da opção que o usuário escolheu no menu <select>.
        # O 'relatorio_escolhido' é o 'name' que demos ao <select> no HTML
        # Cria uma variável vazia para guardar o nome do arquivo que vamos gerar.
        escolha = request.form["relatorio_escolhido"]
        nome_arquivo_gerado = None


        # Agora, verificamos o valor da 'escolha' e chamamos a função
        # correspondente do nosso arquivo "relatorios_graficos.py".
        if escolha == "relatorio_completo":
            nome_arquivo_gerado = relatorios_graficos.gerar_relatorio_completo()
        elif escolha == "relatorio_funcionarios":
            nome_arquivo_gerado = relatorios_graficos.gerar_relatorio_funcionarios()
        elif escolha == "relatorio_exames":
            nome_arquivo_gerado = relatorios_graficos.gerar_relatorio_exames()
        elif escolha == "relatorio_funcao":
            nome_arquivo_gerado = relatorios_graficos.gerar_relatorio_funcao()
        elif escolha == "grafico_funcionarios":
             nome_arquivo_gerado = relatorios_graficos.gerar_graficos_funcionarios()
        elif escolha == "grafico_exames":
             nome_arquivo_gerado = relatorios_graficos.gerar_graficos_exames()
        elif escolha == "grafico_funcao":
            nome_arquivo_gerado = relatorios_graficos.gerar_graficos_funcao()

        # Se a variável "nome_arquivo_gerado" não estiver vazia (ou seja, um relatório foi criado).
        if nome_arquivo_gerado:
            # Nós usamos o 'send_file' para enviar o arquivo gerado
            # de volta ao navegador, o que inicia o download.
            try:
                return send_file(nome_arquivo_gerado, as_attachment=True)
            # Se der erro ele exibe a mensagem de erro no terminal e recarrega página.
            except Exception as e:
                print(f"Erro ao enviar arquivo {e}")
                return redirect(url_for("index"))
        else:
            # Se a função falhou (retornou None) ou a opção não foi implementada,
            # apenas manda o usuário de volta para a página inicial.
            return redirect(url_for("index"))


    # Se alguém tentar acessar "/gerar" sem ser por um formulário (ex: digitando na URL)
    # ele também é enviado de volta para a página inicial.
    return redirect(url_for("index"))


# Este é o comando que de fato "liga" o servidor.
# 'debug=True' é ótimo para nós, pois reinicia o servidor 
# automaticamente toda vez que salvamos o arquivo.
if __name__ == "__main__":
    app.run(debug=True)
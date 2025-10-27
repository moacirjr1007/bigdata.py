from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import relatorios_graficos

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("principal.html")

@app.route("/gerar", methods=["POST"])
def gerar_relatorio():
    
    if request.method == "POST":
        escolha = request.form["relatorio_escolhido"]
        nome_arquivo_gerado = None

        if escolha == "relatorio_completo":
            nome_arquivo_gerado = relatorios_graficos.gerar_relatorio_completo()
        elif escolha == "relatorio_funcionarios":
            nome_arquivo_gerado = relatorios_graficos.gerar_relatorio_funcionarios()
        elif escolha == "relatorio_exames":
            nome_arquivo_gerado = relatorios_graficos.gerar_relatorio_exames()
        elif escolha == "relatorio_funcao":
            nome_arquivo_gerado = relatorios_graficos.gerar_relatorio_funcao()
        elif escolha == "grafico_funcionarios":
            pass
        elif escolha == "grafico_funcao":
            pass

        
        if nome_arquivo_gerado:
            try:
                return send_file(nome_arquivo_gerado, as_attachment=True)
            except Exception as e:
                print(f"Erro ao enviar arquivo {e}")
                return redirect(url_for("index"))
        else:
            return redirect(url_for("index"))

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
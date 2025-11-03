
# 🚀 Display Bird
O Display Bird é uma aplicação web completa desenvolvida em Python, que transforma uma planilha de dados brutos (bigData.xlsx) em relatórios e gráficos de Business Intelligence sob demanda. A interface web permite ao usuário selecionar o tipo de análise desejada, e o backend (Flask + Pandas) processa os dados, gera um novo arquivo .xlsx (seja um relatório ou um gráfico) e o disponibiliza para download imediato.
## 🖥️ Tela Principal

<img width="1919" height="1079" alt="tela" src="https://github.com/user-attachments/assets/939ddbd5-a3c9-415c-ab19-09f5abe06db4" />


## ✨ Funcionalidades

O sistema é capaz de ler múltiplas abas de um arquivo Excel, consolidar os dados e gerar as seguintes análises:

- Relatório Completo: Gera uma visão geral completa de todos os dados do Excel, unificando todas as abas e limpando os espaços em branco.

- Relatório de Funcionários: Cria uma lista organizada de funcionários e suas respectivas datas de exame.

- Relatório de Exames: Gera um relatório simples mostrando quais exames foram realizados e em quais datas.

- Relatório por Função: Mostra quais funções (cargos) tiveram exames realizados e quando, permitindo acompanhar os exames por tipo de função dentro da empresa.

- Gráfico Top 10 Funcionários - Mais Exames Realizados: Mostra quais funcionários mais realizaram exames e quantos foram feitos por cada um, destacando visualmente o ranking dos 10 primeiros.

- Gráfico Top 10 Exames Realizados: Mostra quais são os exames mais comuns realizados no período analisado e quantas vezes cada um aparece.

- Gráfico Top 15 Funções: Mostra quais cargos/funções mais aparecem nos exames e quantos exames foram realizados por cada função.

## 🛠️ Tecnologias Utilizadas

O sistema combina tecnologias de frontend, backend e ciência de dados:

- ### 🗄️ Backend (Servidor):

    - Python 3.13.7: A linguagem principal.

    - Flask: Micro-framework web responsável por:

        - Servir a página HTML (render_template).
        - Definir as rotas (@app.route).
        - Receber os dados do formulário (request).
        - Enviar os arquivos gerados para download (send_file).


- ### 📊 Processamento de Dados e Gráficos:

    - Pandas: A principal ferramenta para ler, concatenar, filtrar e manipular os dados do Excel.

    - Matplotlib: Usada para criar e estilizar os gráficos.

    - Openpyxl: Biblioteca usada para criar e editar arquivos Excel (.xlsx) direto pelo Python.

    - io: Usado como um "arquivo temporário" na memória RAM para salvar a imagem do gráfico antes de passá-la para o  Openpyxl.
    
    - os: Permite interagir com o sistema operacional, como abrir arquivos, criar pastas, verificar caminhos.

- ### 🌐 Frontend (Interface):

    - HTML5: Estrutura semântica da página (incluindo a tag <form>).

    - CSS3: Estilização completa, incluindo:

    - Flexbox: Para centralizar e alinhar os elementos.

    - Media Queries: Para garantir que o layout seja responsivo e funcione bem em celulares (max-width: 768px).

    - Google Fonts: Para as fontes personalizadas ("Audiowide" e "Poppins").

- ### 📦 Ambiente:

    - Virtual Environment (.venv): Para isolar as bibliotecas (Flask, Pandas, etc.) do sistema.


## 📁 Estrutura do Sistema
O projeto segue a estrutura padrão do Flask, que separa a lógica, os templates e os arquivos estáticos:

```
/bigdata.py/
│
├── .venv/                   # Pasta do ambiente virtual com as bibliotecas
├── static/
│   └── estilizacao.css      # Nosso arquivo de estilo (CSS)
│
├── templates/
│   └── principal.html       # Nosso arquivo de interface (HTML)
│
├── README.md                (Este arquivo)
├── app.py                   # O "cérebro" - Servidor Flask e rotas
├── bigData.xlsx             # O arquivo de dados brutos
└── relatorios_graficos.py   # O "trabalho pesado" - Funções com Pandas e Matplotlib
```

## ⚙️ Como Executar o Sistema Localmente: 

- ### Clone o repositório:


```bash
  git clone [https://github.com/moacirjr1007/bigdata.py.git]
  cd bigdata.py
```

- ### Crie e ative o ambiente virtual:

```bash
# Criar
python -m venv .venv

# Ativar (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Ativar (Linux/Mac)
source .venv/bin/activate
Instale as dependências: (Você pode criar um arquivo requirements.txt ou instalar manualmente)

```

- ### Instale as bibliotecas necessárias:

```bash
pip install Flask pandas matplotlib openpyxl
Execute o servidor Flask:
```
- ### Execute o sistema no seu computador:

```bash
python app.py
Acesse no seu navegador: Abra o seu navegador e vá para http://127.0.0.1:5000
```
    
## Autores

- [@moacirjr1007](https://www.github.com/moacirjr1007)


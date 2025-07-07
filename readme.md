# 📊 Gráfico de Pareto - Valor Doado por Personagem

Este projeto gera um gráfico de Pareto com base nos valores doados pelos personagens de um jogo, utilizando dados do banco MySQL.

---

## 🚀 Como funciona

1. Conecta ao banco MySQL e busca os dados das tabelas `accounts`, `players` e `financeiro`.
2. Gera um gráfico de Pareto interativo (HTML) mostrando:
   - Barras: total doado por personagem
   - Linha: porcentagem acumulada (%)
3. Salva o resultado como `pareto.html`

---


## 💻 Como rodar

### 1️⃣ Clone o projeto

git clone https://github.com/seu_usuario/seu_repositorio.git

cd seu_repositorio

2️⃣ Instale as dependências

pip install -r requirements.txt

3️⃣ Crie o arquivo .env
Crie um arquivo chamado .env com as credenciais do banco:

DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=seu_banco

4️⃣ Execute o script

python pareto.py
O gráfico será gerado como pareto.html.


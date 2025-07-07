from sqlalchemy import create_engine
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os

# 📦 Carregar variáveis do ambiente
load_dotenv(dotenv_path="ENV.env")

# 🔑 Variáveis de conexão
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

print(f"Conectado ao banco: {db_name} no host {db_host} com usuário {db_user}")

# 🔗 Cria engine SQLAlchemy + PyMySQL
engine = create_engine(
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
)

# 📝 Query com INNER JOIN para trazer nome_personagem
query = """
SELECT 
    players.name AS nome_personagem,
    financeiro.valor_doado
FROM 
    financeiro
INNER JOIN 
    players ON players.id = financeiro.player_id
WHERE
    financeiro.valor_doado IS NOT NULL
LIMIT 1000;
"""

# 📊 Carrega dados no pandas
df = pd.read_sql(query, engine)

# 🔍 Agrupar no pandas (somar valor_doado por nome_personagem)
df_grouped = (
    df.groupby('nome_personagem', as_index=False)['valor_doado']
    .sum()
    .rename(columns={'valor_doado': 'total_doado'})
    .sort_values(by='total_doado', ascending=False)
)

# 📊 Calcular % acumulado (Pareto)
df_grouped['percentual_acumulado'] = (
    100 * df_grouped['total_doado'].cumsum() / df_grouped['total_doado'].sum()
)

# 📈 Plotar gráfico com Plotly
fig = px.bar(
    df_grouped,
    x='nome_personagem',
    y='total_doado',
    title='Gráfico de Pareto - Valor Doado por Personagem',
    labels={'nome_personagem': 'Nome do Personagem', 'total_doado': 'Total Doado (R$)'}
)

# 📉 Linha do acumulado
fig.add_scatter(
    x=df_grouped['nome_personagem'],
    y=df_grouped['percentual_acumulado'],
    mode='lines+markers',
    name='% Acumulado',
    yaxis='y2'
)

# 🎨 Layout com 2 eixos Y
fig.update_layout(
    yaxis=dict(title='Total Doado (R$)'),
    yaxis2=dict(title='% Acumulado', overlaying='y', side='right', range=[0, 110]),
    xaxis=dict(tickangle=-45, tickmode='linear')
)

# 💾 Salvar como HTML
fig.write_html("pareto.html")
print("✅ Gráfico salvo como pareto.html")

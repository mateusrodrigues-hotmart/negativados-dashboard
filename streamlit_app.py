import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Título
st.title("Usuários Negativados")

# Métrica principal
st.metric("Contagem de Usuários", "11,60 Mil")

# Filtro de ID de Usuário
user_id = st.text_input("USER ID", "")

# Gráfico de rosca para status dos usuários usando Plotly
st.subheader("Contagem de Usuário por Status")
status_data = pd.DataFrame({
    'Status': ['Ativo', 'Inativo', 'Bloqueado'],
    'Quantidade': [11111, 0, 958]
})

fig = px.pie(status_data, values='Quantidade', names='Status', hole=0.4)
st.plotly_chart(fig)

# Slider para Score RBS
st.slider("Score RBS", 0, 710, (0, 710))

# Dropdown para Moeda
currency = st.selectbox("Moeda", ["Todos", "BRL", "USD", "EUR", "ARS", "CLP", "COP", "MXN"])

# Slider para Probabilidade de Negativação
st.slider("Probabilidade de Negativação", 0.0, 100.0, (0.55, 100.0))

# Gráfico de Linha para Evolução do Saldo - 6 meses
st.subheader("Evolução do Saldo - 6 Meses")
time_series_data = pd.DataFrame({
    'Mês': pd.date_range("2024-01-01", periods=6, freq='M'),
    'BRL': np.random.rand(6) * -100,
    'USD': np.random.rand(6) * -200,
    'EUR': np.random.rand(6) * -300,
})
st.line_chart(time_series_data.set_index('Mês'))

# Gráfico de barras para Bloqueios Secundários
st.subheader("Bloqueios Secundários")
treemap_data = pd.DataFrame({
    'Bloqueio': ['BK_NEW_PRODUCTS', 'BLOCK_WITHDRAW', 'BK_REQUEST_AFFILIATE', 'BK_LINKS_SELL_USERS'],
    'Quantidade': [400, 300, 200, 100]
})
st.bar_chart(treemap_data.set_index('Bloqueio'))

# Tabela de dados dos usuários
st.subheader("Dados de Usuários")
user_data = pd.DataFrame({
    'Total Value': [-841345.66, -8.81, -51.98],
    'Currency': ['COP', 'COP', 'COP'],
    'Wallet': ['1666743', '581753', '507976'],
    'User ID': ['HOTMART', 'HOTMART', 'HOTMART'],
    'User Email': ['barbarianr6@gmail.com', 'fegundisandrade@gmail.com', 'andy3n31@hotmail.com'],
    'Status': ['Ativo', 'Ativo', 'Ativo']
})
st.dataframe(user_data)

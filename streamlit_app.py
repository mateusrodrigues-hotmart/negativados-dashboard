import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Usuários Negativados")

# Dividindo o layout
col1, col2 = st.columns([1, 3])

# Coluna da esquerda
with col1:
    st.metric("Contagem de Usuários", "11,60 Mil")

    st.text_input("User ID")
    st.slider("Score RBS", 0, 710, (0, 710))
    st.selectbox("Moeda", ["Todos", "BRL", "USD", "EUR", "ARS", "CLP", "COP", "MXN"])
    st.slider("Probabilidade de Negativação", 0.55, 100.0, (0.55, 100.0))

    # Gráfico de pizza: Contagem por status
    status_data = pd.DataFrame({
        'Status': ['Ativo', 'Inativo', 'Bloqueado'],
        'Quantidade': [11111, 0, 958]
    })
    fig_pie = px.pie(status_data, values='Quantidade', names='Status', hole=0.4, 
                     color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_pie, use_container_width=True)

# Coluna da direita
with col2:
    st.subheader("Evolução do Saldo - 6 Meses")
    time_series_data = pd.DataFrame({
        'Mês': pd.date_range("2024-01-01", periods=6, freq='M'),
        'BRL': np.random.rand(6) * -100,
        'USD': np.random.rand(6) * -200,
        'EUR': np.random.rand(6) * -300,
    })
    fig_line = px.line(time_series_data, x='Mês', y=['BRL', 'USD', 'EUR'],
                       labels={"value": "Saldo Total", "Mês": "Mês"},
                       title="Evolução do Saldo")
    st.plotly_chart(fig_line, use_container_width=True)

# Nova seção para informações adicionais
st.markdown("---")
col3, col4 = st.columns([2, 1])

with col3:
    st.subheader("Dados de Usuários")
    user_data = pd.DataFrame({
        'Total Value': [-841345.66, -8.81, -51.98],
        'Currency': ['COP', 'COP', 'COP'],
        'Wallet': ['1666743', '581753', '507976'],
        'User ID': ['HOTMART', 'HOTMART', 'HOTMART'],
        'User Email': [
            'zedochachimboarianr6@gmail.com', 
            'fegundisandrade@gmail.com', 
            'andy3n31@hotmail.com'
        ],
        'Status': ['Ativo', 'Ativo', 'Ativo']
    })
    st.dataframe(user_data, height=300)

with col4:
    st.subheader("Bloqueios Secundários")
    treemap_data = pd.DataFrame({
        'Bloqueio': ['BK_NEW_PRODUCTS', 'BLOCK_WITHDRAW', 'BK_REQUEST_AFFILIATE', 'BK_LINKS_SELL_USERS'],
        'Quantidade': [400, 300, 200, 100]
    })
    fig_treemap = px.treemap(treemap_data, path=['Bloqueio'], values='Quantidade',
                             title="Bloqueios Secundários", color='Quantidade',
                             color_continuous_scale='blues')
    st.plotly_chart(fig_treemap, use_container_width=True)

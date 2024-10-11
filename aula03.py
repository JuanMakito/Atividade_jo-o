import streamlit as st
import requests
import pandas as pd

st.title("DASHBOARD DE VENDAS :shopping_trolley:")

url = "https://labdados.com/produtos"
response = requests.get(url)

if response.status_code == 200:
    df = pd.DataFrame.from_dict(response.json())
    receita_total = df['Preço'].sum()
    qtd_vendas = len(df)

    receita_total_milhoes = receita_total / 1_000_000  
    qtd_vendas_mil = qtd_vendas / 1_000 

    
    if st.button("Mostrar Todos"):
        st.balloons()
        st.snow()
        col1, col2 = st.columns(2)
        with col1:
            st.metric('Receita Total', f"R$ {receita_total_milhoes:.2f} Milhões")
        with col2:
            st.metric('Quantidade de vendas (linhas)', f"{qtd_vendas_mil:.3f} Mil")
        st.dataframe(df)

    else:
        st.write("Clique no botão Mostrar Todos")
else:
    st.write("Erro ao acessar os dados. Tente novamente.")

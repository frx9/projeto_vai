import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Financeiro", layout="wide")

# Ler Excel
df = pd.read_excel("hype.xlsx", sheet_name="Planilha1")

st.title("📊 Dashboard Financeiro")

# Mostrar tabela
st.subheader("Dados da Planilha")
st.dataframe(df)

# Selecionar trimestre
colunas_periodos = df.columns[3:]

periodo = st.selectbox(
    "Selecione o período",
    colunas_periodos
)

# Gráfico de barras
st.subheader(f"Valores - {periodo}")

fig, ax = plt.subplots(figsize=(12,6))

ax.bar(df["Conta"], df[periodo])

plt.xticks(rotation=45)
plt.ylabel("Valor")
plt.xlabel("Conta")

st.pyplot(fig)

# Pizza dos 5 maiores itens
st.subheader("Participação dos 5 maiores valores")

top5 = df.nlargest(5, periodo)

fig2, ax2 = plt.subplots(figsize=(8,8))

ax2.pie(
    top5[periodo],
    labels=top5["Conta"],
    autopct="%1.1f%%"
)

st.pyplot(fig2)
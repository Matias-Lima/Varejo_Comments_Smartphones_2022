import streamlit as st
import pandas as pd


# Title
st.subheader("Varejo - Smartphones - 2022")
st.title('Comments Per Day Visualization')

# Upload a CSV file
def carregar_dados():
    tabela = pd.read_excel("Comments_counts_Smartphone_2022.xlsx")
    return tabela

with st.container():
    st.write("---")
    final_dataframe = carregar_dados()
    st.area_chart(final_dataframe,x="Date", y="Data")



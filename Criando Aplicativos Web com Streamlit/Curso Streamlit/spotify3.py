import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

# importar dados spotify
df = pd.read_csv("spotify.csv")

# indice = musica
df.set_index("Track", inplace=True)

# título
st.title("Quantidade de :blue[Likes] :sunglasses:")

# botao para selecionar o artista
# artista = st.sidebar.selectbox("Artista: ", df["Artist"].unique())
artista = st.selectbox("Artista: ", df["Artist"].unique())

# checkbox
botao = st.checkbox("Mostrar Gráfico")

# gráfico
if botao: st.bar_chart(df[df["Artist"] == artista]["Likes"])





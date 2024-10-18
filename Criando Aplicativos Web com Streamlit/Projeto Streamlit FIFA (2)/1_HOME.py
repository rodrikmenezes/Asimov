import streamlit as st
import pandas as pd
from datetime import datetime

# titulo
st.markdown("# FIFA DATASET! ⚽")

# assinatura
st.sidebar.markdown("Desenvolvido por :blue[RodriK]")

# corpo do texto
st.markdown(
    """
    O dataset **FIFA 2023** disponível no Kaggle contém informações detalhadas sobre jogadores de futebol, 
    times e estatísticas do jogo. Ele inclui atributos como habilidades, posições, idades, 
    nacionalidades e valores de mercado dos jogadores, além de dados sobre ligas e clubes. 
    Este conjunto de dados é frequentemente utilizado para análises estatísticas, 
    visualizações e para treinos em projetos de machine learning relacionados ao futebol. 
    É uma excelente fonte para quem deseja explorar o desempenho dos jogadores e 
    entender as dinâmicas do futebol profissional.
    """
)

# carregar dados
if "dados" not in st.session_state:
    
    # importar
    df = pd.read_csv("datasets\CLEAN_FIFA23_official_data.csv", index_col=0)
    
    # filtro de jogadores que estão com contrato válido até o presente momento
    df = df[df["Contract Valid Until"] >= datetime.today().year]
    
    # excluir jogadores sem registro de valor
    df = df[df["Value(£)"] > 0]
    
    # ordenar
    df = df.sort_values(by="Overall", ascending=False)
    
    # atribuir df a session state dados
    st.session_state["dados"] = df
    



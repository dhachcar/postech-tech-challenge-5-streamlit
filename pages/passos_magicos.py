import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from tabs.passos_magicos.onu_ods_tab import PassosMagicosONUODSTab
from tabs.passos_magicos.sobre_tab import PassosMagicosSobreTab
from util.constantes import TITULO_PASSOS_MAGICOS, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_PASSOS_MAGICOS} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()


with st.container():
    st.header(f":orange[{TITULO_PASSOS_MAGICOS}]")
    st.image('assets/imgs/logo-passos-magicos.png')

    tab0, tab1 = st.tabs(tabs=["Sobre", "ONU & ODS"])

    PassosMagicosSobreTab(tab0)
    PassosMagicosONUODSTab(tab1)

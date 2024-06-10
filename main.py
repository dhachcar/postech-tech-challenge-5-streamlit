import streamlit as st
from util.constantes import TITULO_PRINCIPAL
from util.layout import output_layout
import warnings
import locale


warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
st.set_page_config(page_title=TITULO_PRINCIPAL, layout="wide")
output_layout()

st.header(f":orange[{TITULO_PRINCIPAL}]")

st.subheader(
    ":blue[Passos Mágicos: o impacto positivo que uma ONG oferece à sociedade]",
    divider="blue",
)
st.markdown(
    """
    REDIGIR INTRODUÇÃO.
"""
)

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
    REDIGIR OBJETIVO.
"""
)

st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
    REDIGIR METODOLOGIA;
"""
)

import pandas as pd
from tabs.modelos_e_redes_neurais.ponto_virada.correlacao_tab import (
    ModelosPrevisaoPontoViradaCorrelacaoTab,
)
from tabs.modelos_e_redes_neurais.ponto_virada.modelo_tab import (
    ModelosPrevisaoPontoViradaModeloTab,
)
from tabs.tab import TabInterface
import streamlit as st
import plotly.graph_objs as go


class ModelosPrevisaoPontoViradaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            tab0, tab1 = st.tabs(tabs=["Correlação", "Modelo"])

            ModelosPrevisaoPontoViradaCorrelacaoTab(tab0)
            ModelosPrevisaoPontoViradaModeloTab(tab1)

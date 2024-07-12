import pandas as pd
from tabs.modelos_e_redes_neurais.indicacao_bolsa.correlacao_tab import (
    ModelosPrevisaoIndicacaoBolsaCorrelacaoTab,
)
from tabs.modelos_e_redes_neurais.indicacao_bolsa.modelo_tab import (
    ModelosPrevisaoIndicacaoBolsaModeloTab,
)
from tabs.tab import TabInterface
import streamlit as st
import plotly.graph_objs as go


class ModelosPrevisaoIndicacaoBolsaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            tab0, tab1 = st.tabs(tabs=["Correlação", "Modelo"])

            ModelosPrevisaoIndicacaoBolsaCorrelacaoTab(tab0)
            ModelosPrevisaoIndicacaoBolsaModeloTab(tab1)

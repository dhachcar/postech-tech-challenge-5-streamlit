import pandas as pd
from tabs.modelos_e_redes_neurais.indicacao_bolsa.correlacao_tab import (
    ModelosPrevisaoIndicacaoBolsaCorrelacaoTab,
)
from tabs.modelos_e_redes_neurais.indicacao_bolsa.modelo_tab import (
    ModelosPrevisaoIndicacaoBolsaModeloTab,
)
from tabs.modelos_e_redes_neurais.indicacao_bolsa.sobre import (
    ModelosPrevisaoIndicacaoBolsaSobreTab,
)
from tabs.tab import TabInterface
import streamlit as st


class ModelosPrevisaoIndicacaoBolsaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            tab0, tab1, tab2 = st.tabs(tabs=["Sobre", "Correlação", "Modelo"])

            ModelosPrevisaoIndicacaoBolsaSobreTab(tab0)
            ModelosPrevisaoIndicacaoBolsaCorrelacaoTab(tab1)
            ModelosPrevisaoIndicacaoBolsaModeloTab(tab2)

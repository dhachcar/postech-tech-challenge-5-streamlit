from tabs.modelos_e_redes_neurais.ponto_virada.modelo_tab import (
    ModelosPrevisaoPontoViradaModeloTab,
)
from tabs.modelos_e_redes_neurais.ponto_virada.sobre_tab import (
    ModelosPrevisaoPontoViradaSobreTab,
)
from tabs.tab import TabInterface
import streamlit as st


class ModelosPrevisaoPontoViradaTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            tab0, tab1 = st.tabs(tabs=["Sobre", "Modelo"])

            # TODO: se der tempo, colocar a matriz de correlação, mas ela deve considerar as colunas processadas por NLP + hotencoder
            ModelosPrevisaoPontoViradaSobreTab(tab0)
            ModelosPrevisaoPontoViradaModeloTab(tab1)

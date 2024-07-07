from tabs.tab import TabInterface
import streamlit as st

class AnaliseIndicadoresTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            x = "TODO: grafico dos indicadores"
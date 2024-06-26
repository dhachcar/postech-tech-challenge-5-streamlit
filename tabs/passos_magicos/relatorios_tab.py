from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class PassosMagicosPEDERelatoriosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                    PEDE + Relatórios
                    TODO: Pesquisa Extensiva do Desenvolvimento Educacional, explicar o que é, os relatorios que existem e permitir o download, colocar as referencias do estudo aqui e na pagina de ref
                """,
                unsafe_allow_html=True,
            )

from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class PassosMagicosBaseDadosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                    Base de dados

                    TODO: falar a respeito da base de dados, os dados anonimizados, quantidade de alunos e a relação dela com o dicionário, disponibilizar link de download da base anonimizada e do dicionario
                    
                """,
                unsafe_allow_html=True,
            )

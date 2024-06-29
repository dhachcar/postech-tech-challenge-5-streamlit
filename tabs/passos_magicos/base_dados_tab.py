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

            with open("assets/materiais/dicionario-dados.pdf", "rb") as file:
                btn = st.download_button(
                    label="Dicionários de dados",
                    data=file,
                    file_name="dicionario-dados-techchallenge5-danilo-achcar.pdf",
                    mime="application/pdf",
                )

            with open("assets/csv/dataset_passos_magicos.csv", "rb") as file:
                btn = st.download_button(
                    label="Base de dados anonimizada",
                    data=file,
                    file_name="base-anonimizada-passos-magicos.csv",
                    mime="text/csv",
                )
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

            with open("assets/materiais/relatorio-pede-2020.pdf", "rb") as file:
                btn = st.download_button(
                    label="Relatório PEDE 2020",
                    data=file,
                    file_name="relatorio-pede-2020-techchallenge5-danilo-achcar.pdf",
                    mime="application/pdf",
                )

            with open("assets/materiais/relatorio-pede-2021.pdf", "rb") as file:
                btn = st.download_button(
                    label="Relatório PEDE 2021",
                    data=file,
                    file_name="relatorio-pede-2021-techchallenge5-danilo-achcar.pdf",
                    mime="application/pdf",
                )

            with open("assets/materiais/relatorio-pede-2022.pdf", "rb") as file:
                btn = st.download_button(
                    label="Relatório PEDE 2022",
                    data=file,
                    file_name="relatorio-pede-2022-techchallenge5-danilo-achcar.pdf",
                    mime="application/pdf",
                )
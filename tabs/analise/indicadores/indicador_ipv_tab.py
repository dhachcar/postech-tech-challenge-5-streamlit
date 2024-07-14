from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
import streamlit as st


class AnaliseIndicadorIPVTab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IPV"
        self.comentario_1_2020 = "TODO: redigir"
        self.comentario_2_2020 = "TODO: redigir"
        self.comentario_1_2021 = "TODO: redigir"
        self.comentario_2_2021 = "TODO: redigir"
        self.comentario_1_2022 = "TODO: redigir"
        self.comentario_2_2022 = "TODO: redigir"
        self.comentario_1_comparacao = "TODO: redigir"
        self.comentario_2_comparacao = "TODO: redigir"

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IPV]**."
            )
            st.info(
                "**Indicador de Ponto de Virada (IPV)**: Segundo o dicionário de dados, é a métrica de Média das Notas de Ponto de Virada do Aluno.",
                icon=":material/help:",
            )

        super().__init__(tab)

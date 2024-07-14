from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
import streamlit as st


class AnaliseIndicadorIAATab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IAA"
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
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IAA]**."
            )
            st.info(
                "**Indicador de Auto Avaliação (IAA)**: Segundo o dicionário de dados, é a métrica de Média das Notas de Auto Avaliação do Aluno.",
                icon=":material/help:",
            )

        super().__init__(tab)

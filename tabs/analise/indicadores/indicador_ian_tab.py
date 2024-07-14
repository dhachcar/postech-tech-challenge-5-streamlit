from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
import streamlit as st


class AnaliseIndicadorIANTab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IAN"
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
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IAN]**."
            )
            st.info(
                "**Indicador de Adequação ao Nível (IAN)**: Segundo o dicionário de dados, é a métrica de Média das Notas de Adequação do Aluno ao nível atual.",
                icon=":material/help:",
            )

        super().__init__(tab)

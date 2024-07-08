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

        # TODO: melhorar estilo e texto introdutorio
        with tab:
            st.markdown('Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno')

        super().__init__(tab)

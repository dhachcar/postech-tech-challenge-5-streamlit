from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
import streamlit as st


class AnaliseIndicadorINDETab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "INDE"
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
            st.markdown('Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV')

        super().__init__(tab)

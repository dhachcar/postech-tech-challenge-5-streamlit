import pandas as pd
from tabs.tab import TabInterface
import streamlit as st

from util.charts import plot_bar, plot_boxplot, plot_histograma


class AnaliseDemograficoInstituicaoTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.df_2020 = pd.read_csv("assets/csv/processado_base_2020.csv", sep=";")
        self.df_2021 = pd.read_csv("assets/csv/processado_base_2021.csv", sep=";")
        self.df_2022 = pd.read_csv("assets/csv/processado_base_2022.csv", sep=";")
    
        self.render()

    def render(self):
        with self.tab:
            st.subheader(f":blue[Instituição de ensino]", divider="blue")
            st.markdown(
                "TODO: redigir"
            )

            st.subheader(f":blue[2020]", divider="blue")
            fig = plot_bar(self.df_2020, 'INSTITUICAO_ENSINO_ALUNO', 'Instituições de ensino dos alunos em 2020', xaxis='Instituição de ensino')
            st.plotly_chart(fig, use_container_width=True)

            with st.expander(":red[Comentários]", expanded=True):
                st.markdown("TODO: redigir")

            st.subheader(f":blue[2021]", divider="blue")
            fig = plot_bar(self.df_2021, 'INSTITUICAO_ENSINO_ALUNO', 'Instituições de ensino dos alunos em 2021', xaxis='Instituição de ensino')
            st.plotly_chart(fig, use_container_width=True)

            with st.expander(":red[Comentários]", expanded=True):
                st.markdown("TODO: redigir")

            st.markdown('**:red[Não há dados disponiveis a respeito das instituições de ensino em 2022 na Passos Mágicos]**')

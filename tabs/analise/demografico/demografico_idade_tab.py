import pandas as pd
from tabs.tab import TabInterface
import streamlit as st
from util.storage import storage_singleton
from util.charts import plot_bar, plot_boxplot, plot_histograma


class AnaliseDemograficoIdadeTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.df_2020 = storage_singleton.df_2020

        self.render()

    def render(self):
        with self.tab:
            st.subheader(f":blue[Idade dos alunos]", divider="blue")
            st.markdown(
                "TODO: falar que temos a idade dos alunos apenas no dataset de 2020 e portanto ele será utilizado"
            )

            # tratativa para idades nulas
            self.df_2020["IDADE_ALUNO"] = pd.to_numeric(
                self.df_2020["IDADE_ALUNO"], errors="coerce"
            )

            total_por_idade = self.df_2020["IDADE_ALUNO"].value_counts().sort_index()
            st.dataframe(total_por_idade)

            with st.expander(":blue[Comentários]", expanded=True):
                st.markdown("TODO: redigir")

            descritivo_idade = self.df_2020["IDADE_ALUNO"].describe()
            st.dataframe(descritivo_idade)

            with st.expander(":blue[Comentários]", expanded=True):
                st.markdown("TODO: redigir")

            fig = plot_bar(
                self.df_2020, "IDADE_ALUNO", "Idade dos alunos", xaxis="Idade"
            )
            st.plotly_chart(fig, use_container_width=True)

            with st.expander(":blue[Comentários]", expanded=True):
                st.markdown("TODO: redigir")

            fig = plot_histograma(
                self.df_2020,
                "IDADE_ALUNO",
                "Distribuição da idade dos alunos",
                rug=False,
            )
            st.plotly_chart(fig, use_container_width=True)

            with st.expander(":blue[Comentários]", expanded=True):
                st.markdown("TODO: redigir")

            fig = plot_boxplot(
                self.df_2020, "IDADE_ALUNO", "Boxplot das idades dos alunos"
            )
            st.plotly_chart(fig, use_container_width=True)

            with st.expander(":blue[Comentários]", expanded=True):
                st.markdown("TODO: redigir")

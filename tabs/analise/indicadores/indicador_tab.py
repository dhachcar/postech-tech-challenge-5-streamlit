from tabs.tab import TabInterface
import streamlit as st
from util.storage import storage_singleton
from util.charts import (
    plot_boxplot,
    plot_boxplot_comparativo,
    plot_histograma,
    plot_histograma_comparativo,
)


class AnaliseIndicadorTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.df_2020 = storage_singleton.df_2020
        self.df_2021 = storage_singleton.df_2021
        self.df_2022 = storage_singleton.df_2022
        self.df_full = storage_singleton.df_full

        self.render()

    def render(self):
        with self.tab:
            self.render_2020()
            self.render_2021()
            self.render_2022()
            self.render_comparacao_ano_a_ano()

    def render_2020(self):
        st.subheader(f":blue[{self.col}: 2020]", divider="blue")

        fig = plot_histograma(self.df_2020, self.col, 2020, analise=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(self.comentario_1_2020)

        fig = plot_boxplot(
            self.df_2020,
            self.col,
            f"Distribuição do {self.col} para o ano de 2020",
            calcular_media=True,
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(self.comentario_2_2020)

    def render_2021(self):
        st.subheader(f":blue[{self.col}: 2021]", divider="blue")

        fig = plot_histograma(self.df_2021, self.col, 2021, analise=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(self.comentario_1_2021)

        fig = plot_boxplot(
            self.df_2021,
            self.col,
            f"Distribuição do {self.col} para o ano de 2021",
            calcular_media=True,
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(self.comentario_2_2021)

    def render_2022(self):
        st.subheader(f":blue[{self.col}: 2022]", divider="blue")

        fig = plot_histograma(self.df_2022, self.col, 2022, analise=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(self.comentario_1_2022)

        fig = plot_boxplot(
            self.df_2022,
            self.col,
            f"Distribuição do {self.col} para o ano de 2022",
            calcular_media=True,
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(self.comentario_2_2022)

    def render_comparacao_ano_a_ano(self):
        st.subheader(
            f":blue[{self.col}: comparativo entre todos os anos]", divider="blue"
        )

        fig = plot_histograma_comparativo(self.df_full, self.col)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown(self.comentario_1_comparacao)

        fig = plot_boxplot_comparativo(self.df_full, self.col)

        st.plotly_chart(fig, use_container_width=True)
        st.markdown(self.comentario_2_comparacao)

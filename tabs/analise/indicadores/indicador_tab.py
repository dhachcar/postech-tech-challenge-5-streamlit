import pandas as pd
from tabs.tab import TabInterface
import streamlit as st

from util.charts import plot_boxplot, plot_histograma


class AnaliseIndicadorTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.df_2020 = pd.read_csv("assets/csv/processado_base_2020.csv", sep=";")
        self.df_2021 = pd.read_csv("assets/csv/processado_base_2021.csv", sep=";")
        self.df_2022 = pd.read_csv("assets/csv/processado_base_2022.csv", sep=";")
        self.df_full = pd.read_csv("assets/csv/processado_base_full.csv", sep=";")

        self.render()

    def render(self):
        with self.tab:
            self.render_2020()
            self.render_2021()
            self.render_2022()

    def render_2020(self):
        st.subheader(f":blue[{self.col}: 2020]", divider="blue")

        fig = plot_histograma(self.df_2020, self.col, 2020)

        st.plotly_chart(fig, use_container_width=True)

        with st.expander(":red[Comentários]", expanded=True):
            st.markdown(self.comentario_1_2020)

        fig = plot_boxplot(
            self.df_2020, self.col, f"Distribuição do {self.col} para o ano de 2020"
        )

        st.plotly_chart(fig, use_container_width=True)

        with st.expander(":red[Comentários]", expanded=True):
            st.markdown(self.comentario_2_2020)

    def render_2021(self):
        st.subheader(f":blue[{self.col}: 2021]", divider="blue")

        fig = plot_histograma(self.df_2021, self.col, 2021)

        st.plotly_chart(fig, use_container_width=True)

        with st.expander(":red[Comentários]", expanded=True):
            st.markdown(self.comentario_1_2021)

        fig = plot_boxplot(
            self.df_2021, self.col, f"Distribuição do {self.col} para o ano de 2021"
        )

        st.plotly_chart(fig, use_container_width=True)

        with st.expander(":red[Comentários]", expanded=True):
            st.markdown(self.comentario_2_2021)

    def render_2022(self):
        st.subheader(f":blue[{self.col}: 2022]", divider="blue")

        fig = plot_histograma(self.df_2022, self.col, 2022)

        st.plotly_chart(fig, use_container_width=True)

        with st.expander(":red[Comentários]", expanded=True):
            st.markdown(self.comentario_1_2022)

        fig = plot_boxplot(
            self.df_2022, self.col, f"Distribuição do {self.col} para o ano de 2022"
        )

        st.plotly_chart(fig, use_container_width=True)

        with st.expander(":red[Comentários]", expanded=True):
            st.markdown(self.comentario_2_2022)
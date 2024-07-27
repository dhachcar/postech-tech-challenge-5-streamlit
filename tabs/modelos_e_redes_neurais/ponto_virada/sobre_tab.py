import pandas as pd
from tabs.tab import TabInterface
import streamlit as st
import plotly.graph_objs as go


class ModelosPrevisaoPontoViradaModeloTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        # TODO: carregar o modelo + scalers tbm
        self.df = pd.read_csv("assets/csv/processado_base_ml_pv.csv", sep=";")

        self.render()

    def predict(self, texto):
        x = 1
        # texto_tokenizado = self.tokenizer(texto)
        # text_vect = self.vect.transform([texto_tokenizado])
        # pred = self.modelo.predict(text_vect)

        # st.markdown(pred)

    def render(self):
        with self.tab:
            st.markdown(
                f"""Modelo criado utilizando XGBoost""",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""A proposta deste modelo é identificar quais alunos podem podem atingir o seu Ponto de Virada.""",
                unsafe_allow_html=True,
            )


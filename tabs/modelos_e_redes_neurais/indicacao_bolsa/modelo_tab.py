import joblib
from tabs.tab import TabInterface
import streamlit as st
from keras.models import load_model
import pandas as pd
import numpy as np


class ModelosPrevisaoIndicacaoBolsaModeloTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.modelo = load_model("assets/modelos/perceptron/multilayer-perceptron")
        self.scaler = joblib.load("assets/modelos/perceptron/scaler.pkl")

        self.render()

    def predict(self, aluno: pd.DataFrame):
        aluno_scaled = self.scaler.transform(aluno)
        pred = self.modelo.predict(aluno_scaled)

        if pred.round()[0] > 0:
            st.balloons()
            st.success(":white_check_mark: **Recomendação:** o aluno **está apto** à receber a bolsa de estudos :grinning:")
        else:
            st.error(":x: **Recomendação:** o aluno **não está apto** à receber a bolsa de estudos :disappointed:")

    def render(self):
        with self.tab:
            col0, col1, col2, col3 = st.columns(4)

            with col0:
                indicador_inde = st.number_input(
                    label="**:blue[INDE]**",
                    key="inde",
                    min_value=0.0,
                    max_value=10.0,
                    value=0.0,
                    step=0.1,
                    format="%.2f",
                )

            with col1:
                indicador_ian = st.number_input(
                    label="**:blue[IAN]**",
                    key="ian",
                    min_value=0.0,
                    max_value=10.0,
                    value=0.0,
                    step=0.1,
                    format="%.2f",
                )

            with col2:
                indicador_ida = st.number_input(
                    label="**:blue[IDA]**",
                    key="ida",
                    min_value=0.0,
                    max_value=10.0,
                    value=0.0,
                    step=0.1,
                    format="%.2f",
                )

            with col3:
                indicador_ieg = st.number_input(
                    label="**:blue[IEG]**",
                    key="ieg",
                    min_value=0.0,
                    max_value=10.0,
                    value=0.0,
                    step=0.1,
                    format="%.2f",
                )

            col0, col1, col2, col3 = st.columns(4)

            with col0:
                indicador_iaa = st.number_input(
                    label="**:blue[IAA]**",
                    key="iaa",
                    min_value=0.0,
                    max_value=10.0,
                    value=0.0,
                    step=0.1,
                    format="%.2f",
                )

            with col1:
                indicador_ips = st.number_input(
                    label="**:blue[IPS]**",
                    key="ips",
                    min_value=0.0,
                    max_value=10.0,
                    value=0.0,
                    step=0.1,
                    format="%.2f",
                )

            with col2:
                indicador_ipp = st.number_input(
                    label="**:blue[IPP]**",
                    key="ipp",
                    min_value=0.0,
                    max_value=10.0,
                    value=0.0,
                    step=0.1,
                    format="%.2f",
                )

            with col3:
                indicador_ipv = st.number_input(
                    label="**:blue[IPV]**",
                    key="ipv",
                    min_value=0.0,
                    max_value=10.0,
                    value=0.0,
                    step=0.1,
                    format="%.2f",
                )

            aluno = pd.DataFrame(
                {
                    "IAA": [indicador_iaa],
                    "IAN": [indicador_ian],
                    "IDA": [indicador_ida],
                    "IEG": [indicador_ieg],
                    "INDE": [indicador_inde],
                    "IPP": [indicador_ipp],
                    "IPS": [indicador_ips],
                    "IPV": [indicador_ipv],
                }
            )

            if st.button(":crystal_ball: Prever", key="btn_predict_lstm"):
                with st.spinner("Processando..."):
                    st.subheader(":blue[Matriz de entrada do modelo]", divider="blue")
                    st.dataframe(aluno, hide_index=True)

                    st.subheader(":blue[Previsão do modelo]", divider="blue")
                    self.predict(aluno)

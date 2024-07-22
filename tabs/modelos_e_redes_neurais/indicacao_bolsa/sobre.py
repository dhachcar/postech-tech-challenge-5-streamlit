import pandas as pd
from tabs.tab import TabInterface
import streamlit as st
import plotly.graph_objs as go
import numpy as np


class ModelosPrevisaoIndicacaoBolsaSobreTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.epochs = np.array(range(2000))
        self.training = pd.read_csv(
            "assets/modelos/perceptron/model_training_data_hist.csv", sep=";"
        )

        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                f"""Modelo criado utilizando um Multilayer Perceptron""",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""A proposta deste modelo é identificar quais alunos podem ser recomendados para receber uma bolsa de estudos. Utilizamos dados históricos de 2022 (os únicos disponíveis) e dados simulados para melhorar a base de treinamento. Os dados simulados seguiram o critério de que notas menores ou iguais a 5 desclassificam o aluno, enquanto notas iguais ou superiores a 8 garantem a recomendação para a bolsa. A decisão para notas intermediárias fica a cargo do modelo, utilizando os dados de treinamento.""",
                unsafe_allow_html=True,
            )

            col0, col1 = st.columns(2)

            with col0:
                fig = go.Figure()

                fig.add_trace(
                    go.Scatter(
                        x=self.epochs,
                        y=self.training["accuracy"],
                        mode="lines",
                        name="Acurácia de Treinamento",
                    )
                )
                fig.add_trace(
                    go.Scatter(
                        x=self.epochs,
                        y=self.training["val_accuracy"],
                        mode="lines",
                        name="Acurácia de Validação",
                        line=dict(color="red"),
                    )
                )

                fig.update_layout(
                    title="Performance do modelo - Acurácia (accuracy)",
                    xaxis_title="Época",
                    yaxis_title="Valor",
                    height=600,
                    xaxis=dict(range=[0, 2000]),
                )

                st.plotly_chart(fig, use_container_width=True)

            with col1:
                fig = go.Figure()

                fig.add_trace(
                    go.Scatter(
                        x=self.epochs,
                        y=self.training["loss"],
                        mode="lines",
                        name="Perda de Treinamento",
                    )
                )
                fig.add_trace(
                    go.Scatter(
                        x=self.epochs,
                        y=self.training["val_loss"],
                        mode="lines",
                        name="Perda de Validação",
                        line=dict(color="red"),
                    )
                )

                fig.update_layout(
                    title="Performance do modelo - Perda (loss)",
                    xaxis_title="Época",
                    yaxis_title="Valor",
                    height=600,
                    xaxis=dict(range=[0, 2000]),
                )

                st.plotly_chart(fig, use_container_width=True)

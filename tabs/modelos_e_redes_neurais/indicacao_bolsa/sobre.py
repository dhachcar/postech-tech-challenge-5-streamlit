import pandas as pd
from tabs.tab import TabInterface
import streamlit as st
import plotly.graph_objs as go
import numpy as np

from util.layout import format_number


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
                f"""A proposta deste modelo **:blue[(um MLP ou Multilayer Perceptron)]** é identificar quais alunos podem ser recomendados para receber uma bolsa de estudos. Utilizamos dados históricos de **:blue[2022]** (os únicos disponíveis) e dados simulados para melhorar a base de treinamento. Os dados simulados seguiram o critério de que notas menores ou iguais a **:blue[5]** desclassificam o aluno, enquanto notas iguais ou superiores a **:blue[8]** garantem a recomendação para a bolsa. A decisão para notas intermediárias fica a cargo do modelo, utilizando os dados de treinamento.""",
                unsafe_allow_html=True,
            )

            # 2000/2000 [04:09<00:00,  8.88epoch/s, loss=0.245, accuracy=0.887, val_loss=0.228, val_accuracy=0.898]
            loss_treinamento = format_number(0.245 * 100, "%0.2f")
            loss_validacao = format_number(0.228 * 100, "%0.2f")
            acuracia_treinamento = format_number(0.887 * 100, "%0.2f")
            acuracia_validacao = format_number(0.898 * 100, "%0.2f")

            st.subheader(":blue[Indicadores do modelo]", divider="blue")
            st.markdown(
                f"""
                O modelo de recomendação de bolsas de estudo desenvolvido para a ONG  **:blue[Passos Mágicos]** foi avaliado em termos de desempenho utilizando métricas de perda (loss) e acurácia (accuracy). Os resultados obtidos durante o treinamento e a validação podem ser observados a seguir:
                * Loss no treinamento: **:blue[{loss_treinamento}%]**
                * Acurácia no treinamento: **:blue[{acuracia_treinamento}%]**
                * Loss na validação: **:blue[{loss_validacao}%]**
                * Acurácia na validação: **:blue[{acuracia_validacao}%]**

                Os dados de performance demonstram que o modelo está generalizando bem para dados ainda não vistos, o que indica que ele não apresenta nenhum problema de *overfitting*.
                """,
                unsafe_allow_html=True,
            )

            with st.container():
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
                        legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1,
                        ),
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
                        legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1,
                        ),
                    )

                    st.plotly_chart(fig, use_container_width=True)

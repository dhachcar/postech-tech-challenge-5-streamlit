import pandas as pd
from tabs.tab import TabInterface
import streamlit as st
import plotly.graph_objs as go


class ModelosPrevisaoIndicacaoBolsaCorrelacaoTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.matriz_correlacao = pd.read_csv(
            "assets/csv/processado_base_ml_bolsa_corr.csv", sep=";"
        )

        self.render()

    def render(self):
        with self.tab:
            # plot do heatmap (correlação)
            fig = go.Figure(
                data=go.Heatmap(
                    z=self.matriz_correlacao.values[::-1],
                    x=self.matriz_correlacao.columns,
                    y=self.matriz_correlacao.columns[::-1],
                    colorbar=dict(title="Correlação"),
                    colorscale="matter",
                    xgap=1,
                    ygap=1,
                )
            )

            fig.update_layout(title="Matriz de correlação", height=600, width=700)
            fig.update_layout(xaxis_side="top", xaxis=dict(tickangle=-25))

            st.plotly_chart(fig)

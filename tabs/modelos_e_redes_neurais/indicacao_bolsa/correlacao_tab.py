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
            st.markdown(
                """
                Nesta seção, apresentamos a correlação das features utilizadas para a criação do modelo. Basicamente foram utilizados os indicadores de performance e podemos observar uma certa correlação entre alguns indicadores com **:blue[INDE]**. Outros indicadores que fazem parte de um mesmo agrupamento (p.ex.: **:blue[IPP]** e **:blue[IPV]**) também possuem uma correlação maior (apesar de correlação não implicar causalidade). Por fim, temos também a correlação com a feature de **:blue[INDICADO_BOLSA]**, o que parece não estabelecer nenhuma relação direta com outras features. Isso demonstra ainda mais a necessidade de um método padronizado para concessão de bolsas para os melhores alunos, método o qual é proposto pelo modelo criado.
            """,
                unsafe_allow_html=True,
            )

            # plot do heatmap (correlação)
            fig = go.Figure(
                data=go.Heatmap(
                    z=self.matriz_correlacao.values[::-1],
                    x=self.matriz_correlacao.columns,
                    y=self.matriz_correlacao.columns[::-1],
                    colorbar=dict(title="Correlação"),
                    colorscale="Viridis",
                    xgap=1,
                    ygap=1,
                )
            )

            fig.update_layout(title="Matriz de correlação", height=600, width=700)
            fig.update_layout(xaxis_side="top", xaxis=dict(tickangle=-25))

            st.plotly_chart(fig)

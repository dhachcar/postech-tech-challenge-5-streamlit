import time
from tabs.tab import TabInterface
import streamlit as st
from util.storage import storage_singleton
import plotly.graph_objects as go
from st_aggrid import AgGrid, GridOptionsBuilder


class AnaliseAlunosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.indicadores = ["IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]
        self.df = storage_singleton.df_full[
            ["NOME", "ANO", "INDE", "IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]
        ]
        self.page = 1
        self.pag_rows_per_page = 50
        self.pag_total_pages = len(self.df) // self.pag_rows_per_page + (
            len(self.df) % self.pag_rows_per_page > 0
        )

        self.render()

    def plot_radar(self, valores):
        fig = go.Figure()

        fig.add_trace(
            go.Scatterpolar(
                r=valores,
                theta=self.indicadores,
                fill="toself",
                name="Grupo 1",
                fillcolor="rgba(0, 123, 255, 0.3)",  # Cor azul com 30% de opacidade
                line=dict(
                    color="rgba(0, 123, 255, 1)"
                ),  # Cor da borda azul totalmente opaca
            )
        )

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 10]),
                bgcolor="rgba(255, 255, 255, 0)",  # Fundo do polar plot transparente
            ),
        )

        return fig

    def output_dataframe(self):
        with st.spinner("Processando..."):
            time.sleep(3)

            # Definir o número de linhas por página
            rows_per_page = 50

            # Calcular o número total de páginas
            total_pages = len(self.df) // rows_per_page + (
                len(self.df) % rows_per_page > 0
            )

            # Calcular os índices de início e fim para o DataFrame
            start_idx = (self.page - 1) * rows_per_page
            end_idx = start_idx + rows_per_page

            # Mostrar o DataFrame paginado
            df_paginado = self.df.iloc[start_idx:end_idx]

            gob = GridOptionsBuilder.from_dataframe(df_paginado)
            gob.configure_default_column(cellStyle={"textAlign": "center"})
            gob.configure_grid_options(
                suppressHorizontalScroll=True
            )
            grid_options = gob.build()

            st.markdown(
                f"""
                <span style='float: left'>Página :blue[{self.page}] de :blue[{total_pages}]</span>
                <small style='float: right'>Para **:blue[navegar entre as abas]**, posicione o mouse em cima das abas e segure a tecla **:blue[[SHIFT]]** e utilize botão central de scroll do mouse :three_button_mouse:</small>
                """,
                unsafe_allow_html=True,
            )

            AgGrid(df_paginado, gridOptions=grid_options, fit_columns_on_grid_load=True)
            st.success("Processamento concluído! :white_check_mark:")

            # st.dataframe(, use_container_width=True, column_config=)

    def render(self):
        with self.tab:
            st.subheader(":blue[Alunos]")

            col0, col1, _ = st.columns([2, 2, 6])

            with col0:
                self.page = st.number_input(
                    "Página", min_value=1, max_value=self.pag_total_pages, value=1
                )

            with col1:
                anos = self.df["ANO"].unique()
                self.filtro_ano = st.selectbox("Ano", key="filtro_ano", options=list(anos))

            self.output_dataframe()

            # for index, row in self.df.iterrows():
            #     st.write(row["NOME"], row[self.indicadores])
            #     if st.button(f"Atualizar Gráfico para '{row['NOME']}'"):
            #         radar_fig = self.plot_radar(self.df[self.indicadores].values)
            #         st.plotly_chart(radar_fig)

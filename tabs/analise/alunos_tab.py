import time
from tabs.tab import TabInterface
import streamlit as st
import pandas as pd
from util.layout import format_number
from util.storage import storage_singleton
import plotly.graph_objects as go


class AnaliseAlunosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.page = 1
        self.indicadores = ["IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]
        self.pag_rows_per_page = 50
        self.df = storage_singleton.df_full[
            ["NOME", "ANO", "INDE", "IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]
        ]
        self.pag_total_pages = len(self.df) // self.pag_rows_per_page + (
            len(self.df) % self.pag_rows_per_page > 0
        )

        self.render()

    def plot_radar(self, aluno: str, indicadores: pd.DataFrame):
        fig = go.Figure()

        fig.add_trace(
            go.Scatterpolar(
                r=indicadores.values,
                theta=indicadores.keys(),
                fill="toself",
                name=f"Performance dos indicadores - {aluno}",
                fillcolor="rgba(0, 123, 255, 0.3)",
                line=dict(color="rgba(0, 123, 255, 1)"),
            )
        )

        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 10]),
                bgcolor="rgba(255, 255, 255, 0)",
            ),
        )

        return fig

    def output_dataframe(self):
        with st.spinner("Processando..."):
            time.sleep(1)

            # linhas por pagina
            rows_per_page = 50

            st.write(self.page)

            # determina o df para filtro
            df_para_filtro = (
                self.df.query(f"ANO == {self.filtro_ano}")
                if self.filtro_ano != 0
                else self.df
            )

            # faz o cálculo da qtd total de páginas
            total_pages = len(df_para_filtro) // rows_per_page + (
                len(df_para_filtro) % rows_per_page > 0
            )

            # faz o cálculo da janela paginada
            start_idx = (self.page - 1) * rows_per_page
            end_idx = start_idx + rows_per_page

            # processa o df considerando a paginação
            df_paginado = df_para_filtro.iloc[start_idx:end_idx]

            st.markdown(
                f"""
                <span style='float: left'>Página :blue[{self.page}] de :blue[{total_pages}]</span>
                <small style='float: right'>Para **:blue[navegar entre as abas]**, posicione o mouse em cima das abas e segure a tecla **:blue[[SHIFT]]** e utilize botão central de scroll do mouse :three_button_mouse:</small>
                """,
                unsafe_allow_html=True,
            )

            # formatações do dataframe
            # IMPORTANTE: aqui faço uma cópia para formatar os campos na cópia e não no original, pois posteriormente, preciso dos valores numéricos no gráfico de radar
            df_paginado_output = df_paginado.copy()

            df_paginado_output["ANO"] = df_paginado["ANO"].apply(
                lambda x: format_number(x, "%0.0f")
            )

            df_paginado_output[self.indicadores] = df_paginado[self.indicadores].applymap(
                lambda x: format_number(x, "%0.2f")
            )

            # output do df
            df_index_selecionado = st.dataframe(
                df_paginado_output,
                hide_index=True,
                use_container_width=True,
                on_select="rerun",
                selection_mode="single-row",
            )
            index_selecionado = df_index_selecionado.selection.rows[0] if len(df_index_selecionado.selection.rows) > 0 else None

            # plot do gráfico de radar
            if index_selecionado != None:
                selecionado = df_paginado.iloc[index_selecionado]
                fig = self.plot_radar(aluno=selecionado["NOME"], indicadores=selecionado[self.indicadores])
                st.plotly_chart(fig)

            st.success("Processamento concluído! :white_check_mark:")

    def render(self):
        with self.tab:
            st.subheader(":blue[Alunos]")

            col0, col1, _ = st.columns([2, 2, 6])

            with col0:
                self.page = st.number_input(
                    "Página",
                    min_value=1,
                    max_value=self.pag_total_pages,
                    value=self.page,
                )

            with col1:
                # constroi a lista de anos, com a opção 'Todos'
                anos = {0: "Todos"}
                for i in self.df["ANO"].unique():
                    anos[i] = i

                # selectbox
                self.filtro_ano = st.selectbox(
                    "Ano",
                    key="filtro_ano",
                    options=list(anos),
                    format_func=(lambda x: anos[x]),
                )

            self.output_dataframe()

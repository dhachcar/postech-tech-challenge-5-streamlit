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

        if "page" not in st.session_state:
            st.session_state["page"] = 1

        if "ano_filtrado" not in st.session_state:
            st.session_state["ano_filtrado"] = 0

        self.pag_rows_per_page = 50
        self.indicadores = ["IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]
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
            page = int(st.session_state["page"])
            ano_filtrado = int(st.session_state["ano_filtrado"])

            # determina o df para filtro
            df_para_filtro = (
                self.df.query(f"ANO == {ano_filtrado}")
                if ano_filtrado != 0
                else self.df
            )

            # faz o cálculo da qtd total de páginas
            total_pages = len(df_para_filtro) // self.pag_rows_per_page + (
                len(df_para_filtro) % self.pag_rows_per_page > 0
            )

            # faz o cálculo da janela paginada
            start_idx = (page - 1) * self.pag_rows_per_page
            end_idx = start_idx + self.pag_rows_per_page

            # processa o df considerando a paginação
            df_paginado = df_para_filtro.iloc[start_idx:end_idx]

            st.markdown(
                f"Página :blue[{page}] de :blue[{total_pages}]",
                unsafe_allow_html=True,
            )

            # formatações do dataframe
            # IMPORTANTE: aqui faço uma cópia para formatar os campos na cópia e não no original, pois posteriormente, preciso dos valores numéricos no gráfico de radar
            df_paginado_output = df_paginado.copy()

            df_paginado_output["ANO"] = df_paginado["ANO"].apply(
                lambda x: format_number(x, "%0.0f")
            )

            df_paginado_output[self.indicadores] = df_paginado[
                self.indicadores
            ].applymap(lambda x: format_number(x, "%0.2f"))

            col0, col1 = st.columns([7, 3])

            with col0:
                # output do df
                df_index_selecionado = st.dataframe(
                    df_paginado_output,
                    hide_index=True,
                    use_container_width=True,
                    on_select="rerun",
                    selection_mode="single-row",
                )

                st.markdown(
                    """<small>**:blue[Clique na primeira coluna (vazia)]** :three_button_mouse: na tabela acima para **:blue[selecionar um aluno]** e visualizar o seu respectivo gráfico de performance dos indicadores</small>""",
                    unsafe_allow_html=True,
                )

                st.image("assets/imgs/aluno-selecao-exemplo.png")

                st.divider()

                index_selecionado = (
                    df_index_selecionado.selection.rows[0]
                    if len(df_index_selecionado.selection.rows) > 0
                    else None
                )

            with col1:
                # plot do gráfico de radar
                if index_selecionado != None:
                    selecionado = df_paginado.iloc[index_selecionado]
                    fig = self.plot_radar(
                        aluno=selecionado["NOME"],
                        indicadores=selecionado[self.indicadores],
                    )
                    st.plotly_chart(fig)

            st.success("Processamento concluído! :white_check_mark:")

    def render(self):
        with self.tab:
            st.subheader(":blue[Alunos]")

            col0, col1, _ = st.columns([2, 2, 6])

            with col0:
                page = st.number_input(
                    "Página",
                    min_value=1,
                    max_value=self.pag_total_pages,
                    step=1,
                    key="input_page",
                    value=int(st.session_state["page"]),
                    help="Selecione a página que deseja visualizar",
                )

                st.session_state["page"] = page

            with col1:
                # constroi a lista de anos, com a opção 'Todos'
                anos = {0: "Todos"}
                for i in self.df["ANO"].unique():
                    anos[i] = i

                # selectbox
                st.session_state["ano_filtrado"] = st.selectbox(
                    "Ano",
                    key="input_ano",
                    options=list(anos),
                    format_func=(lambda x: anos[x]),
                    on_change=self.reset_paginacao,
                    help="Selecione o ano de filtro do dataset",
                )

            self.output_dataframe()

    # TODO: tem um bug nesse reset... em alguns momentos ele redefine a pagina para 1 em outros não
    def reset_paginacao(self):
        # st.session_state["page"] = 1
        if "page" in st.session_state:
            st.session_state.update({'page': 1})

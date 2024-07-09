import time
from tabs.tab import TabInterface
import streamlit as st
import pandas as pd
from util.storage import storage_singleton
import plotly.graph_objects as go
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode


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



        # Dados de exemplo
        data = {
            'Nome': ['Alice', 'Bob', 'Charlie', 'David'],
            'Idade': [25, 30, 35, 40],
            'Salário': [50000, 60000, 75000, 90000]
        }

        # DataFrame inicial
        df = pd.DataFrame(data)

        # Exibir o DataFrame
        st.write("Dados:", df)

        # Verifica se uma linha foi selecionada
        linha_selecionada = st.session_state.get('linha_selecionada', None)

        if linha_selecionada is not None:
            # Obtém os dados da linha selecionada
            dados_linha = df.iloc[linha_selecionada]
            
            # Exibe o gráfico com os dados da linha selecionada
            st.subheader(f"Dados para {dados_linha['Nome']} (Idade: {dados_linha['Idade']}, Salário: {dados_linha['Salário']})")
            
            # Aqui você pode plotar qualquer gráfico com base nos dados da linha selecionada
            # Vamos criar um gráfico de linha simples para ilustrar
            dados_grafico = pd.DataFrame({
                'Categoria': ['Idade', 'Salário'],
                'Valor': [dados_linha['Idade'], dados_linha['Salário']]
            })

            st.line_chart(dados_grafico.set_index('Categoria'))

        # Adiciona uma função para clicar na linha
        for i, row in df.iterrows():
            if st.button(f"Clique para {row['Nome']}"):
                st.session_state['linha_selecionada'] = i






        self.render()

    def plot_radar(self, valores):
        fig = go.Figure()

        fig.add_trace(
            go.Scatterpolar(
                r=valores,
                theta=self.indicadores,
                fill="toself",
                name="Grupo 1",
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

            st.dataframe(df_para_filtro, hide_index=True, use_container_width=True)

            # faz o cálculo da qtd total de páginas
            total_pages = len(df_para_filtro) // rows_per_page + (
                len(df_para_filtro) % rows_per_page > 0
            )

            # faz o cálculo da janela paginada
            start_idx = (self.page - 1) * rows_per_page
            end_idx = start_idx + rows_per_page

            # processa o df considerando a paginação
            df_paginado = df_para_filtro.iloc[start_idx:end_idx]

            # botão de ação das linhas da tabela
            action_cell_renderer = JsCode(
                """
                class ActionCellRenderer {
                    init(params) {
                        this.params = params;
                        
                        this.eGui = document.createElement('button');
                        this.eGui.style.background = 'none';
                        this.eGui.style.padding = '0 10px';
                        this.eGui.style.lineHeight = '15px';
                        this.eGui.style.border = '1px solid #fff';
                        this.eGui.innerHTML = 'Ver +';

                        this.eGui.addEventListener('click', function() {
                            // TODO: como passar isso para o grafico
                            // params.data = contém os dados da linha

                            fetch('', {method: 'POST'}).then(response => {
                                if (!response.ok) {
                                    throw new Error('Erro durante o retorno da resposta');
                                }
                                return response.json();
                            }).then(data => {
                                console.log('Gráfico recarregado');
                            }).catch(error => {
                                console.error('Houve um problema com a solicitação fetch:', error);
                            });
                        });
                    }
                    getGui() {
                        return this.eGui;
                    }
                }
                """
            )

            # configs da tabela
            gob = GridOptionsBuilder.from_dataframe(df_paginado)
            gob.configure_default_column(cellStyle={"textAlign": "center"})
            gob.configure_grid_options(suppressHorizontalScroll=True)
            gob.configure_column("Ação", cellRenderer=action_cell_renderer)
            grid_options = gob.build()

            st.markdown(
                f"""
                <span style='float: left'>Página :blue[{self.page}] de :blue[{total_pages}]</span>
                <small style='float: right'>Para **:blue[navegar entre as abas]**, posicione o mouse em cima das abas e segure a tecla **:blue[[SHIFT]]** e utilize botão central de scroll do mouse :three_button_mouse:</small>
                """,
                unsafe_allow_html=True,
            )

            # output da tabela com AgGrid
            AgGrid(
                df_paginado,
                gridOptions=grid_options,
                allow_unsafe_jscode=True,
                fit_columns_on_grid_load=True,
                theme="streamlit",
                enable_enterprise_modules=False,
            )

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
                # constroi a lista de anos, com a opção Todos
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

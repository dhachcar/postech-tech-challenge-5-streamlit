from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
import streamlit as st
from util.layout import format_number
from util.storage import storage_singleton
from util.charts import plot_bar
from util.st_utils import (
    output_pedra_agata,
    output_pedra_ametista,
    output_pedra_quartzo,
    output_pedra_topazio,
)


class AnalisePedraTab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab

        self.cor_quartzo = "#FFB6C1"
        self.cor_agata = "#FF6347"
        self.cor_ametista = "#9966CC"
        self.cor_topazio = "#FFD700"
        self.df_2020 = storage_singleton.df_2020
        self.df_2021 = storage_singleton.df_2021
        self.df_2022 = storage_singleton.df_2022

        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                O indicador INDE relaciona a performance do aluno a pedras preciosas, tornando a avaliação algo mais significativo e motivador. Cada pedra representa uma faixa específica de desempenho, trazendo um elemento de valor e prestígio ao progresso acadêmico. Aqui estão as faixas de desempenho e as pedras correspondentes:
            """
            )

            with st.container():
                col0, col1, col2, col3 = st.columns(4)

                with col0:
                    st.subheader(":blue[1º: Quartzo]", divider="blue")
                    output_pedra_quartzo(width=120)
                    st.markdown(
                        """Para alunos com desempenho entre **:blue[2,405]** e **:blue[5,506]**. O quartzo, uma pedra comum mas essencial, simboliza os primeiros passos no aprendizado, onde a base de conhecimento está sendo firmemente estabelecida."""
                    )

                with col1:
                    st.subheader(":blue[2º: Ágata]", divider="blue")
                    output_pedra_agata(width=120)
                    st.markdown(
                        """Alunos com desempenho de **:blue[5,506]** a **:blue[6,868]** são representados pela ágata. Com suas belas bandas e variedades de cores, a ágata simboliza o crescimento e a diversificação do conhecimento e habilidades."""
                    )

                with col2:
                    st.subheader(":blue[3º: Ametista]", divider="blue")
                    output_pedra_ametista(width=120)
                    st.markdown(
                        """Aqueles com desempenho entre **:blue[6,868]** e **:blue[8,230]** são associados à ametista. Sua cor vibrante e propriedades únicas refletem a criatividade e a profundidade do entendimento que o aluno alcançou."""
                    )

                with col3:
                    st.subheader(":blue[4º: Topázio]", divider="blue")
                    output_pedra_topazio(width=120)
                    st.markdown(
                        """Com desempenho entre **:blue[8,230]** e **:blue[9,294]**, o topázio representa os alunos que alcançaram excelência acadêmica. Esta pedra preciosa, conhecida por sua clareza e brilho, reflete o esforço e a dedicação excepcionais do aluno."""
                    )

            st.markdown(
                """Ao usar essas pedras preciosas como indicadores de desempenho, o INDE não só mede o sucesso acadêmico de maneira clara, mas também inspira os alunos a buscarem níveis mais altos de realização, associando seu progresso a símbolos tangíveis de valor e beleza."""
            )

            with st.container():
                st.subheader(":blue[2020]", divider="blue")
                st.markdown(
                    """
                        Em **:blue[2020]**, muitos alunos conquistaram a pedra de **:blue[Ametista]**, representando um nível elevado de realização acadêmica. Isto demonstra que estes alunos possui uma ótima média de INDE, girando em torno de **:blue[7]** à **:blue[8]**. Entretanto, poucos alunos conseguiram atingir a pedra de **:blue[Tópazio]** (acima de **:blue[8,2]**), o que **:blue[não]** representa algo ruim necessariamente, mas apenas que tal pedra é reservada apenas para os alunos que superarem todas as expectativas em seus estudos.<br/><br/>
                        Se levarmos em consideração que em 2020 o mundo estava enfrentando a pandemia de COVID-19 e todas as criaças estavam sendo afastadas do convívio social (incluindo das escolas), a quantidade de alunos com ótimas índices de INDE impressiona.
                    """,
                    unsafe_allow_html=True,
                )

                cores = [
                    self.cor_ametista,
                    self.cor_agata,
                    self.cor_quartzo,
                    self.cor_topazio,
                ]
                fig = plot_bar(
                    df=self.df_2020,
                    col="PEDRA",
                    titulo="Distribuição das pedras dos alunos em 2020",
                    xaxis="Tipo de pedra",
                    cores=cores,
                )

                st.plotly_chart(fig)

            with st.container():
                total_2020 = len(storage_singleton.df_2020)
                total_2021 = len(storage_singleton.df_2021)
                total_2022 = len(storage_singleton.df_2022)
                proporcao_2021_x_2020 = (
                    f"{format_number((total_2021 * 100) / total_2020, '%0.2f')}%"
                )
                proporcao_2021_x_2022 = (
                    f"{format_number((total_2021 * 100) / total_2022, '%0.2f')}%"
                )

                st.subheader(":blue[2021]", divider="blue")
                st.markdown(
                    f"""
                        Em **:blue[2021]** foi considerado uma quantidade menor de alunos na análise, com cerca de **:red[{proporcao_2021_x_2020}]** do total em relação à 2020 e **:red[{proporcao_2021_x_2022}]** do total em relação à 2022. Proporcionalmente falando, podemos observar uma diminuição nas pedras de **:blue[Quartzo]** e um leve aumenta nas pedras de **:blue[Tópazio]**, o que pode significar que alunos que estavam com a pedra de **:blue[Ametista]** evoluiram ainda mais e conseguiram atingir o último nível, ao mesmo tempo que a quantidade de alunos no primeiro nível diminuiu proporcionalmente ao resto.
                    """,
                    unsafe_allow_html=True,
                )

                cores = [
                    self.cor_ametista,
                    self.cor_agata,
                    self.cor_quartzo,
                    self.cor_topazio,
                ]
                fig = plot_bar(
                    df=self.df_2021,
                    col="PEDRA",
                    titulo="Distribuição das pedras dos alunos em 2021",
                    xaxis="Tipo de pedra",
                    cores=cores,
                )

                st.plotly_chart(fig)

            with st.container():
                st.subheader(":blue[2022]", divider="blue")
                st.markdown(
                    """Por fim, em **:blue[2022]** podemos observar um aumento generalizado em todas os tipos de pedras, com exceção da **:blue[Ametista]** que manteve sua quantidade levemente estável. Aqui também vale reforçar que foi o ano com a maior quantidade de alunos considerados na análise. Além de termos um dataset maior, podemos observar também um aumento expressivo na quantidade de pedras do tipo **:blue[Ágata]**, fato que demonstra que em 2022 as atividades escolares também estavam iniciando o seu retorno à normalidade, e que no período de quarentena imposto pela pandemia de COVID-19, os alunos tiveram um desempenho levemente inferior ao de outros anos, já que a pedra de **:blue[Ágata]** requer um INDE de **:blue[5,5]** à **:blue[6.8]** e foi a que teve o maior aumento, visualizando proporcionalmente.""",
                    unsafe_allow_html=True,
                )

                cores = [
                    self.cor_ametista,
                    self.cor_agata,
                    self.cor_quartzo,
                    self.cor_topazio,
                ]
                fig = plot_bar(
                    df=self.df_2022,
                    col="PEDRA",
                    titulo="Distribuição das pedras dos alunos em 2022",
                    xaxis="Tipo de pedra",
                    cores=cores,
                )

                st.plotly_chart(fig)

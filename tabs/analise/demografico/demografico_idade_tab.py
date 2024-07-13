import pandas as pd
from tabs.tab import TabInterface
import streamlit as st
from util.layout import format_number
from util.storage import storage_singleton
from util.charts import plot_bar, plot_boxplot, plot_histograma


class AnaliseDemograficoIdadeTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.df_2020 = storage_singleton.df_2020

        self.render()

    def render(self):
        with self.tab:
            st.subheader(f":blue[Análise descritiva da idade]", divider="blue")

            # tratativa para idades nulas
            self.df_2020["IDADE_ALUNO"] = pd.to_numeric(
                self.df_2020["IDADE_ALUNO"], errors="coerce"
            )

            # cria uma faixa etária
            bins = [7, 10, 15, 21]
            labels = ["7-9", "10-14", "15+"]
            self.df_2020["FAIXA"] = pd.cut(
                self.df_2020["IDADE_ALUNO"], bins=bins, labels=labels, right=False
            )

            col = "IDADE_ALUNO"
            df_descritiva = self.df_2020[col].to_frame().describe()
            medida_count = format_number(df_descritiva.loc["count"][col])
            medida_mean = format_number(df_descritiva.loc["mean"][col], "%0.2f")
            medida_std = format_number(df_descritiva.loc["std"][col])
            medida_min = format_number(df_descritiva.loc["min"][col])
            medida_25 = format_number(df_descritiva.loc["25%"][col])
            medida_50 = format_number(df_descritiva.loc["50%"][col])
            medida_75 = format_number(df_descritiva.loc["75%"][col])
            medida_max = format_number(df_descritiva.loc["max"][col])
            df_descritiva.reset_index(inplace=True)
            df_descritiva.columns = ["Medida", "Idade"]

            st.markdown(
                f"""A tabela a seguir apresenta uma análise estatística das idades dos alunos, exclusivamente do ano de **:blue[2020]** (o único disponível para análise em relação à idade). Com um total de **:blue[{medida_count}]** observações, a média das idades é de aproximadamente **:blue[{medida_mean}]** anos, com um desvio padrão de **:blue[{medida_std}]** anos, indicando a variação das idades em relação à média. A idade mínima registrada é **:blue[{medida_min}]** anos, enquanto a máxima é **:blue[{medida_max}]** anos. Além disso, **:blue[25%]** dos alunos têm até **:blue[{medida_25}]** anos, a mediana das idades é **:blue[{medida_50}]** anos, e **:blue[75%]** dos alunos têm até **:blue[{medida_75}]** anos, proporcionando uma visão clara sobre a distribuição etária dos alunos em **:blue[2020]**."""
            )

            with st.container():
                _, col, _ = st.columns([3, 4, 3])

                with col:
                    st.divider()
                    st.dataframe(
                        df_descritiva, use_container_width=True, hide_index=True
                    )

            st.subheader(f":blue[Distribuição das idades]", divider="blue")
            st.markdown(
                """Nas próximas seções, analisaremos a distribuição das idades dos alunos, de forma a obtermos insights valiosos."""
            )

            fig = plot_bar(
                self.df_2020,
                "IDADE_ALUNO",
                "Idade dos alunos",
                xaxis="Faixa",
            )

            st.plotly_chart(fig, use_container_width=True)

            total_alunos_10_14_anos = len(
                self.df_2020.query("IDADE_ALUNO >= 10 & IDADE_ALUNO <= 14")
            )
            total_alunos_15mais_anos = len(self.df_2020.query("IDADE_ALUNO >= 15"))
            total_alunos = len(self.df_2020)
            proporcao_1 = (
                format_number(total_alunos_10_14_anos / total_alunos * 100, "%0.2f")
                + "%"
            )
            proporcao_2 = (
                format_number(total_alunos_15mais_anos / total_alunos * 100, "%0.2f")
                + "%"
            )

            st.markdown(
                f"""Conforme podemos observar no gráfico acima, boa parte dos alunos atendidos pela **:blue[Passos Mágicos]** possui idade entre **:blue[10]** e **:blue[14]** anos, com cerca de **:blue[{proporcao_1}]** do total, portanto o maior impacto da ONG pode ser observado em crianças que estão da metade para o fim do Ensino Fundamental. Os alunos mais velhos (**:blue[15+]** anos) também são impactados pela ONG, mas em quantidade inferior à faixa de alunos mais jovens, com cerca de **:blue[{proporcao_2}]** do total."""
            )

            fig = plot_histograma(
                self.df_2020,
                "IDADE_ALUNO",
                "Distribuição da idade dos alunos (%)",
                rug=False,
            )

            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                "No histograma acima, podemos observar melhor a distribuição percentual de alunos em cada idade. Conforme pontuado anteriormente, a faixa com mais alunos gira em torno de **:blue[10]** à **:blue[14]** anos. Este dado também é corroborado pela média e mediana que foram apresentadas na seção anterior."
            )

            fig = plot_boxplot(
                self.df_2020, "IDADE_ALUNO", "Boxplot das idades dos alunos"
            )
            st.plotly_chart(fig, use_container_width=True)

            st.markdown(
                "Por fim, nesta última seção, temos um boxplot que representa de forma visual alguns dados apresentados na análise descritiva anterior, também confirmando os pontos levantados anteriormente."
            )

from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
from util.layout import format_number
from util.storage import storage_singleton
import streamlit as st


class AnaliseIndicadorIAATab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IAA"

        desc_2020 = storage_singleton.df_2020[self.col].describe()
        desc_2021 = storage_singleton.df_2021[self.col].describe()
        desc_2022 = storage_singleton.df_2022[self.col].describe()

        median_2020 = format_number(desc_2020.loc["50%"], "%0.2f")
        mean_2020 = format_number(desc_2020.loc["mean"], "%0.2f")
        q1_2020 = format_number(desc_2020.loc["25%"], "%0.2f")
        q3_2020 = format_number(desc_2020.loc["75%"], "%0.2f")

        median_2021 = format_number(desc_2021.loc["50%"], "%0.2f")
        mean_2021 = format_number(desc_2021.loc["mean"], "%0.2f")
        q1_2021 = format_number(desc_2021.loc["25%"], "%0.2f")
        q3_2021 = format_number(desc_2021.loc["75%"], "%0.2f")

        median_2022 = format_number(desc_2022.loc["50%"], "%0.2f")
        mean_2022 = format_number(desc_2022.loc["mean"], "%0.2f")
        q1_2022 = format_number(desc_2022.loc["25%"], "%0.2f")
        q3_2022 = format_number(desc_2022.loc["75%"], "%0.2f")

        self.comentario_1_2020 = f"""No primeiro ano analisado, podemos observar que grande parte dos alunos, consideram seus desempenhos bem satisfatórios, o que não necessariamente é uma verdade e pode entrar em conflito com outros indicadores, especialmente com os de avaliação efetuada pelos professores. A média de **:blue[{mean_2020}]** e mediana **:blue[{median_2020}]** demonstra este otimismo com os desempenhos apresentados. Vale também mencionar algumas notas **:blue[0]**, o que implica que alguns alunos foram mais críticos e realistas com seus desempenhos (considerados insuficientes) e acabaram zerando na autoavaliação."""

        self.comentario_2_2020 = f"""A visão acima corrobora visualmente as observações estudadas que os alunos julgam seus desempenhos como ótimos. Na questão dos intervalos interquartílicos, temos que Q1 gira em torno de **:blue[{q1_2020}]** e o Q3 fica por volta de **:blue[{q3_2020}]**."""

        self.comentario_1_2021 = f"""Para **:blue[2021]**, tivemos um aumento na quantidade de alunos que se autoavaliaram com **:blue[0]**. Isso pode ser interpretado de 2 maneiras distintas: a primeira, onde o aluno tem a consciência que não está performando de forma adequada ou a segunda (e mais óbvia) que simplesmente foram observados mais casos de alunos zerando do que alunos com notas maiores que **:blue[0]** (o que também é totalmente plausível)."""

        self.comentario_2_2021 = f"""Comparando os dados apresentados acima, podemos observar medidas de tendência central menores que em 2020, com a média em **:blue[{mean_2021}]**, mediana em **:blue[{median_2021}]**, Q1 em **:blue[{q1_2021}]** e Q3 em **:blue[{q3_2021}]** para **:blue[2021]**."""

        self.comentario_1_2022 = f"""No último ano analisado (**:blue[2022]**), a tendência de autoavaliação com uma nota alta voltou a ter uma leve alta se comparado ao ano anterior, mas ainda abaixo dos patamares de **:blue[2020]**."""

        self.comentario_2_2022 = f"""Por fim temos o boxplot e gráfico de dispersão do ano em questão. A respeito das medidas de análise descritiva, foram calculados conforme à seguir: média de **:blue[{mean_2022}]**, mediana de **:blue[{median_2022}]**, Q1 de **:blue[{q1_2022}]** e Q3 de **:blue[{q3_2022}]**."""

        self.comentario_1_comparacao = f"""Nos gráficos apresentados acima, são apresentados os dados dos anos estudados de forma cumulativa. Podemos observar, principalmente no segundo gráfico, a quantidade menor de notas de autoavaliação mais altas, representado pelas barras mais à esquerda e em azul escuro, conforme discutido nas seções anteriores. Apesar disso, na próxima seção iremos observar que a mediana de **:blue[2021]** é maior que as dos demais anos, mesmo tendo a média tomando o sentido inverso (menor que dos demais)."""
 
        self.comentario_2_comparacao = f"""Aqui temos os boxplots comparativos de cada ano. Podemos observar, que dada as distribuições, as análises descritivas são bem próximas umas das outras (talvez com exceção para **:blue[2020]** que aparente ter a caixa do boxplot um pouco abaixo dos demais). E conforme dito anteriormente, **:blue[2021]** tem uma média menor de notas de autoavaliação, mas possui uma mediana superior aos demais anos de estudo."""

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IAA]**."
            )
            st.info(
                "**Indicador de Auto Avaliação (IAA)**: Segundo o dicionário de dados, é a métrica de Média das Notas de Auto Avaliação do Aluno.",
                icon=":material/help:",
            )

        super().__init__(tab)

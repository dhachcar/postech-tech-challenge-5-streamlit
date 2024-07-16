from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
from util.layout import format_number
from util.storage import storage_singleton
import streamlit as st


class AnaliseIndicadorIDATab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IDA"

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

        self.comentario_1_2020 = f"""Para o primeiro ano analisado, podemos observar uma distribuição bem heterogênea. Muitos alunos tivera o **:blue[{self.col}]** em **:blue[0]** e muitos outros (frequência ligeiramente maior) em **:blue[10]**. Também temos um setor denso entre as notas **:blue[7,5]** e **:blue[8]** com uma alta frequência. Isso significa que existem diversos alunos, cada um com suas particularidades, nível e jornada no ensino. Para os alunos com nota 0, podemos levantar a hipótese de que o público-alvo atendido pela **:blue[Passos Mágicos]** são crianças e jovens de baixa renda, que muitas vezes não possuem condições sociais e econômicas de terem um estudo de qualidade em suas vidas e isso pode refletir na quantidade de notas **:blue[0]**."""

        self.comentario_2_2020 = f"""A seguir, temos o boxplot da distribuição de **:blue[2020]** junto da dispersão das observações. Aqui fica evidente o quão dispersas estão as notas dos alunos. Aqui temos uma média em torno de **:blue[{mean_2020}]**, uma mediana em torno de **:blue[{median_2020}]**. Para os intervalos interquartílicos, temos o Q1 com o valor aproximado de **:blue[{q1_2020}]** e o Q3 com o valor de **:blue[{q3_2020}]**."""

        self.comentario_1_2021 = f"""Para o ano de **:blue[2021]**, é visível que houve uma "normalização" da curva, com menos alunos com nota **:blue[0]**, mas com frequências maiores em outras notas baixas (p.ex.: entre e **:blue[1]** e **:blue[4]**), o que acaba puxando as medidas de tendência central para baixo. Também podemos observar um frequência menor no intervalo de notas mais altos (acima de **:blue[8]**), o que também colabora com uma performance pior se comparada ao ano anterior."""

        self.comentario_2_2021 = f"""No boxplot, temos a confirmação das afirmações feitas anteriormente. Temos mais observações no gráfico de dispersão em notas de **:blue[2]** a **:blue[4]** e uma concentração de observações mais abundante no intervalo de **:blue[5]** a **:blue[7]**. Na questão das medidas de têndencia central, temos a média em **:blue[{mean_2021}]** (menor em quase 1 unidade ao ano anterior), a mediana em **:blue[{median_2021}]**, o Q1 em **:blue[{q1_2021}]** e o Q3 em **:blue[{q3_2021}]**. Uma outra explicação para este desempenho mais fraco pode ser atribuido à pandemia de COVID-19, que em **:blue[2021]** atingia o seu maior pico em Abril daquele ano e impactou ainda mais o ensino na época."""

        self.comentario_1_2022 = f"""Em **:blue[2022]**, temos uma retomada do desempenho dos alunos, com as notas do intervalo mais baixo (entre **:blue[0]** e **:blue[4]**), com menores frequências o que favorece uma melhora nas medidas de tendência central. Ainda assim, este ano fica atrás na questão de performance se comparado à **:blue[2020]**, mas à frente de **:blue[2021]**. Aqui o cenário já havia mudado bastante, com a sociedade amplatamente vacinada, as pessoas estavam começando a retomar a normalidade em suas vidas e consequentemente os estudos também foram afetados."""

        self.comentario_2_2022 = f"""Para o boxplot, temos os seguintes da análise descrita: média em **:blue[{mean_2022}]**, mediana em **:blue[{median_2022}]**, intervalo Q1 em **:blue[{q1_2022}]** e intervalor Q3 em **:blue[{q3_2022}]**."""

        self.comentario_1_comparacao = f"""Nos 2 gráficos acima, podemos observar as porcentagens cumulativas das distribuições anuais. No primeiro gráfico, em **:blue[2021]**, podemos observar que a acumulação entre as notas **:blue[8]** e **:blue[10]** é menor se comparada aos outros anos. Enquanto na nota **:blue[8]**, já havia sido atingido o valor de **:blue[94,43%]** da amostra para **:blue[2021]**, em **:blue[2020]** esse valor era de apenas **:blue[69,05%]** e em **:blue[2021]** era de **:blue[85,61%]**."""

        self.comentario_2_comparacao = f"""Por fim, temos os boxplots e gráficos de dispersão comparativos, onde é possível observar uma maior concentração de observações na faixa inferior de notas em **:blue[2021]**, corroborando a performance mais baixa das medidas de tendência central."""

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IDA]**."
            )
            st.info(
                "**Indicador de Aprendizagem (IDA)**: Segundo o dicionário de dados, é a métrica de Média das Notas do Indicador de Aprendizagem.",
                icon=":material/help:",
            )

        super().__init__(tab)

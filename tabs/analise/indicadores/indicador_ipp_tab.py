from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
from util.layout import format_number
from util.storage import storage_singleton
import streamlit as st


class AnaliseIndicadorIPPTab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IPP"

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

        self.comentario_1_2020 = f"""Em **:blue[2020]**, temos um grande quantidade de observações na faixa entre **:blue[7]** e **:blue[8,5]**. Isto demonstra que de forma geral, boa parte dos alunos tiveram notas satisfatórias no quésito psicopedagógico. Também temos algus casos outliers com notas **:blue[10]** ou com notas muito baixas (abaixo de **:blue[3]** p.ex.)."""

        self.comentario_2_2020 = f"""Acima, temos o gráfico de dispersão dos eventos observados junto do boxplot contendo a análise descritiva da distribuição. Podemos observar que de fato, a grande maioria das observações ocorre na faixa entre **:blue[7]** e **:blue[8,5]**. Em questão de valores médios, temos o seguinte: média em **:blue[{mean_2020}]**, mediana em **:blue[{median_2020}]**, Q1 em **:blue[{q1_2020}]** e Q3 em **:blue[{q3_2020}]**."""

        self.comentario_1_2021 = f"""Para **:blue[2021]**, temos um padrão de distribuição parecido, mas com uma concentração maior ainda na mesma faixa já mencionanda anteriormente, de **:blue[7]** a **:blue[8,5]**. Na próxima seção com o boxplot e o gráfico de dispersão, esta concentração fica mais evidente."""

        self.comentario_2_2021 = f"""Conforme observamos e corroborando o que foi descrito anteriormente, há uma grande concentração de observações em torno da faixa de nota **:blue[8]**, mais concentrado ainda que em **:blue[2020]**. Por termos essa maior concentração numa faixa mais alta, a média do ano foi superior à de **:blue[2020]**. Também podemos observar uma mediana maior com uma amplitude menor na variação dos valores auferidos. Em termos de análise descritiva, temos a média em **:blue[{mean_2021}]**, a mediana em **:blue[{median_2021}]**, o Q1 em **:blue[{q1_2021}]** e o Q3 em **:blue[{q3_2021}]**."""

        self.comentario_1_2022 = f"""Por fim, em **:blue[2022]**, podemos observar um distribuição mais "heterogênea", começando por volta da nota **:blue[4]** e se mantendo até por volta da nota **:blue[9]**. Essa dispersão maior dos dados também impacta as medidas de tendência central, principalmente em relação à média."""

        self.comentario_2_2022 = f"""Nos gráficos acima, podemos observar essa distribuição mais ampla, que acabou inclusive impactando negativamente o valor da média que foi inferior aos 2 últimos anos analisados. A mediana também foi ligeiramente menor se comparada aos anos anteriores. De forma geral, temos os seguintes valores da análise: média em **:blue[{mean_2022}]**, mediana em **:blue[{median_2022}]**, Q1 em **:blue[{q1_2022}]** e Q3 em **:blue[{q3_2022}]**."""

        self.comentario_1_comparacao = f"""Os gráficos acima representam as distribuições analisadas de forma cumulativa e cumulativa normalizada, respectivamente. O insight mais vísivel é a respeito da amplitude dos valores nas amostras de **:blue[2022]**, que foi muito superior se comparado aos outros anos."""

        self.comentario_2_comparacao = f"""E aqui, apresentamos os boxplots comparativos dos anos estudados. Novamente, é visível a grande variação de valores para **:blue[2022]**, principalmente quando comparamos com **:blue[2021]**, onde a mioria das observações ficou concentrada nos patamares mais altos de notas."""

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IPP]**."
            )
            st.info(
                "**Indicador Psicopedagógico (IPP)**: Segundo o dicionário de dados, é a métrica de Média das Notas Psicopedagógicas do Aluno.",
                icon=":material/help:",
            )

        super().__init__(tab)

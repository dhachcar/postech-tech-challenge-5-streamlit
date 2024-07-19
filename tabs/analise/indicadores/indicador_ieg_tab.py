from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
from util.layout import format_number
from util.storage import storage_singleton
import streamlit as st


class AnaliseIndicadorIEGTab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IEG"

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

        self.comentario_1_2020 = f"""Para **:blue[2020]**, podemos observar no gráfico acima que boa parte das notas de engajamento ficaram acima de **:blue[8]**, o que demonstra um alto grau de interesse por parte dos alunos atendidos pela ONG."""

        self.comentario_2_2020 = f"""No boxplot e gráfico de dispersão acima podemos observar boa parte parte das observações estão acima da faixa de **:blue[7,5]**, fato o qual representa um engajamento altíssimo. Com uma mediana de **:blue[{median_2020}]** e média de **:blue[{mean_2020}]**, a hipotése para tal valor é que após o início da pandemia de COVID-19, os alunos estavam focados devido à "novidade" dos estudos à distância. Infelizmente o "foco" tende a cair nos próximos anos, conforme será observado. Por fim, para este ano em específico, temos o Q1 em **:blue[{q1_2020}]** e o Q3 em **:blue[{q3_2020}]**, valores que também podem ser considerados como altos."""

        self.comentario_1_2021 = f"""Em **:blue[2021]**, observamos uma queda acentuada nas notas de forma geral e como dito anteriormente, podemos atribuir o pior engajamento em partes pela comodidade que os alunos atingiram durante a pandemia, o que pode ter lhes causado um aumento na falta de interesse, mesmo que continuassem matriculados na ONG."""

        self.comentario_2_2021 = f"""Acima, podemos observar este fenômeno, onde a média para o ano foi **:blue[{mean_2021}]** e a mediana ficou em **:blue[{median_2021}]**. Os intervalos interquartílicos ficam como: Q1 em **:blue[{q1_2021}]** e Q3 em **:blue[{q3_2021}]**. Visivelmente, valores menores se comparados ao ano passado."""

        self.comentario_1_2022 = f"""Por fim, no ano de **:blue[2022]**, temos uma retomada do índice de engajamento geral dos alunos, superando em especial o ano anterior, principalmente se levarmos em consideração as medidas de tendência central. Se compararmos em relação à **:blue[2020]**, a média foi levemente superior, mas a mediana e os intervalos interquartílicos foram menores, o que demonstra uma recuperação em curso do interesse e engajamento dos alunos."""

        self.comentario_2_2022 = f"""Nos visões acima, são apresentados as observações para o ano em questão junto da análise descritiva. Assim, para **:blue[2022]** temos os seguintes valores: média em **:blue[{mean_2022}]**, mediana em **:blue[{median_2022}]**, Q1 em **:blue[{q1_2022}]** e por fim Q3 em **:blue[{q3_2022}]**."""

        self.comentario_1_comparacao = f"""Podemos observar nos 2 gráficos acima, os 3 anos analisados anteriormente de forma agrupada, utilizando a densidade de probabilidade cumulativa, o que facilita a visualização da frequência conforme as notas analisadas vão aumentando. Podemos observar por exemplo, que o ano de **:blue[2021]** (em azul escuro), possui a maior quantidade de observações em notas nas faixas mais baixas, enquanto que em **:blue[2020]**, houveram frequências cumulativas maiores nas faixas intermediárias, o que definitivamente causou o aumento geral das medidas de tendência central, se comparados com **:blue[2022]**."""

        self.comentario_2_comparacao = f"""E aqui, apresentamos boxplots individuais por ano, de forma a exemplificar visualmente as distribuições estudadas."""

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IEG]**."
            )
            st.info(
                "**Indicador de Engajamento (IEG)**: Segundo o dicionário de dados, é a métrica de Média das Notas de Engajamento do Aluno.",
                icon=":material/help:",
            )

        super().__init__(tab)

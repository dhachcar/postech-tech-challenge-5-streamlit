from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
from util.layout import format_number
from util.storage import storage_singleton
import streamlit as st


class AnaliseIndicadorIANTab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IAN"

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

        self.comentario_1_2020 = f"""Para **:blue[2020]**, o **:blue[{self.col}]** apresenta uma distribuição bimodal, com 2 concentrações bem aparentes no valor **:blue[5]** e **:blue[10]**, respectivamente."""

        self.comentario_2_2020 = f"""Acima temos o boxplot do ano analisado junto da distribuição de valores observados após a limpeza e tratamento dos dados. Para o Q1 **:blue[{q1_2020}]**, para o Q3 **:blue[{q3_2020}]**, tendo a média em **:blue[{mean_2020}]** e a mediana em **:blue[{median_2020}]**. Curiosamente, todos os anos possuem a mesma mediana, conforme será demonstrado nas próximas seções."""

        self.comentario_1_2021 = f"""Da mesma forma que no ano anterior, temos uma distribuição bimodal, mas agora com um média ligeiramente menor."""

        self.comentario_2_2021 = f"""O boxplot apresenta os seguintes valores de interesse: Q1 em **:blue[{q1_2021}]**, Q3 em **:blue[{q3_2021}]**, média em **:blue[{mean_2021}]** e mediana em **:blue[{median_2021}]**."""

        self.comentario_1_2022 = f"""Para o último analisado, voltamos a apresentar uma distribuição bimodal. Os picos sempre ficam em torno dos valores **:blue[5]** e **:blue[10]**, provavelmente devido ao método de coleta empregado para este indicador."""

        self.comentario_2_2022 = (
            f"""No boxplot temos os seguintes valores para a análise descritiva: Q1 em **:blue[{q1_2022}]**, Q3 em **:blue[{q3_2022}]**, média em **:blue[{mean_2022}]** e por fim, mediana em **:blue[{median_2022}]**. Vale observar que a média diminuiu novamente em relação ao anterior (**:blue[2022]** X **:blue[2021]**)."""
        )

        self.comentario_1_comparacao = f"""Os gráficos acima demonstram a evolução do índice de forma comparativa entre os anos. Podemos observar as mudanças e evolução nos valores em 3 pontos principais: no primeiro patamar, próximo ao valor **:blue[3]**, no segundo patamar, próximo do valor **:blue[5]** e no último patamar, próximo do valor **:blue[10]**. Esses 3 valores são os únicos encontrados para este indicador, demonstrando que possivelmente existe alguma regra de negócio específica para esta avaliação. Exemplificando melhor, é como se a nota **:blue[3]** representasse uma classificação do tipo **:blue["Não Atende"]**, a nota **:blue[5]** representa um **:blue["Atende"]** e a nota **:blue[10]** representa um **:blue["Supera Expectativas"]**."""

        self.comentario_2_comparacao = f"""Por fim, apresentamos os boxplots comparativos de todos os anos. Podemos ver claramente as observações do **:blue[{self.col}]** concentradas nos valores **:blue[3]**, **:blue[5]** e **:blue[10]**."""

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IAN]**."
            )
            st.info(
                "**Indicador de Adequação ao Nível (IAN)**: Segundo o dicionário de dados, é a métrica de Média das Notas de Adequação do Aluno ao nível atual.",
                icon=":material/help:",
            )

        super().__init__(tab)

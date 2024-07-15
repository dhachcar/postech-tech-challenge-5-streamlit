from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
from util.layout import format_number
from util.storage import storage_singleton
import streamlit as st


class AnaliseIndicadorINDETab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "INDE"

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

        self.comentario_1_2020 = f"""No ano **:blue[2020]**, podemos observar que o valor médio para o índice **:blue[{self.col}]** girou em torno de **:blue[7,5]** e **:blue[8]**. Isso demonstra que a ponderação feita entre todos os outros indicadores, resultou num valor médio alto. O Q1 ficou em **:blue[{q1_2020}]** e o Q3 ficou em **:blue[{q3_2020}]**. A média ficou em **:blue[{mean_2020}]** e a mediana em **:blue[{median_2020}]**."""

        self.comentario_2_2020 = f"""Acima, apresentamos o boxplot contendo a análise descritiva do **:blue[{self.col}]** junto da dispersão dos valores que o compõem."""

        self.comentario_1_2021 = f"""Para **:blue[2021]**, a maior concentração no histograma ficou em torno de **:blue[7]** à **:blue[7,5]**. Um pouco menor se comparado à **:blue[2020]**, mas em contrapartida houve uma concentração maior nas faixas superiores de valores. Ainda assim, **:blue[2021]** teve o pior desempenho geral, entre todos os anos analisados."""

        self.comentario_2_2021 = f"""Da mesma forma, que nos outros anos, apresentamos o boxplot junto da dispersão de valores. Podemos observar um Q1 em **:blue[{q1_2021}]**, um Q3 em **:blue[{q3_2021}]**, junto de uma média em torno de **:blue[{mean_2021}]** e uma mediana em **:blue[{median_2021}]** (os dois últimos, abaixo dos outros anos analisados)."""

        self.comentario_1_2022 = f"""No último ano analisado, o {self.col} foi superior à 2021 mas inferior à 2020 (melhor ano na análise considerando as medidas de tendência central)."""

        self.comentario_2_2022 = f"""Por fim, mostramos o boxplot contendo a análise descritiva. Os valores apresentados são: Q1 em torno de **:blue[{q1_2022}]**, Q3 em torno de **:blue[{q3_2022}]**, média em torno de **:blue[{mean_2022}]** e mediana em **:blue[{median_2022}]**."""

        self.comentario_1_comparacao = f"""Nos 2 gráficos acima, apresentamos a mesma informação de maneira distintas. No primeiro ela vai se acumulando conforme as faixas de notas até atingir o valor máximo de 1 e no segundo os valores são atribuídos em colunas normalizadas para 100% da área disponível.<br/><br/>.
        Um fato relevante que corrobora a média e mediana menores para **:blue[2021]** é que há mais valores menores na faixa entre **:blue[3]** e **:blue[5]**, o que com certeza acabou impactando o valor final."""

        self.comentario_2_comparacao = f"""Por fim, temos um boxplot comparativo entre todos os anos, junto de um gráfico de dispersão com todas as ocorrências auferidas. Para **:blue[2021]**, podemos observar a cauda mais alongada dos quartis, principalmente em relação ao Q1 e o Q2 (mediana), o que justifica as medidas de tendência centrais menores."""

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[INDE]**."
            )
            st.info(
                "**Índice do Desenvolvimento Educacional (INDE)**: Segundo o dicionário de dados, é a métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores IAN, IDA, IEG, IAA, IPS, IPP e IPV.",
                icon=":material/help:",
            )

        super().__init__(tab)

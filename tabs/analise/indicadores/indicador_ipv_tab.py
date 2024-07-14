from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
from util.layout import format_number
from util.storage import storage_singleton
import streamlit as st


class AnaliseIndicadorIPVTab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IPV"

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

        self.comentario_1_2020 = f"Para o ano de **:blue[2020]** podemos observar que a grande maioria dos alunos obteve uma nota que ficou entre **:blue[{q1_2020}]** (Q1) e **:blue[{q3_2020}]** (Q3), o que demonstra notas acima da média de forma geral."
        self.comentario_2_2020 = f"Nesta seção, apresentamos um boxplot dos dados contendo a análise descritiva. A métrica que mais chama a atenção é a mediana, que gira em torno de **:blue[{median_2020}]**, um valor bem alto se considerarmos toda a distribuição, o que indica que os professores dos alunos de fato veem o impacto positivo da ONG na vida das crianças e jovens com aumento de sua performance acadêmica. Já para a média, o valor atingido foi de **:blue[{mean_2020}]**"
        self.comentario_1_2021 = f"""Para o ano de **:blue[2021]** a mediana (e consequentemente a média) geral foi superior à **:blue[2020]**. Portanto, podemos concluir que neste ano os alunos tiveram uma performance melhor que no ano anterior. A maior parte das notas ficou dentro do intervalo de **:blue[{q1_2021}]** (Q1) e **:blue[{q3_2021}]** (Q3). Também vale notar que o Q1 do indicador neste ano foi levemente menor que no ano anterior, mas em contrapartida o Q3 também acabou sendo maior, "alongando" o intervalo de valores."""
        self.comentario_2_2021 = f"O boxplot deste ano corrobora o fato que os valores apresentados foram superiores se comparados ao ano anterior, o que demonstra uma ligeira evolução dos alunos. Para a mediana temos o valor de **:blue[{median_2021}]** e para a média o valor de **:blue[{mean_2021}]**."
        self.comentario_1_2022 = f"Para **:blue[2022]** (último ano da análise), os valores são ligeiramente inferiores aos de **:blue[2021]** e **:blue[2020]**. Podemos inclusive perceber uma variação nas notas superiores à 8, que tiveram uma frequência menor se comparada aos outros anos."
        self.comentario_2_2022 = f"Considerando o boxplot, para a mediana temos o valor de **:blue[{median_2022}]** e para a média o valor de **:blue[{mean_2022}]**. Na questão dos quartis, o Q1 apresenta o valor **:blue[{q1_2022}]** e o Q3 o valor de **:blue[{q3_2022}]**. Não há uma causa direta do porquê os alunos performaram menos neste ano, possivelmente representando uma variação normal entre os anos de estudo."
        self.comentario_1_comparacao = "TODO: redigir"
        self.comentario_2_comparacao = "TODO: redigir"

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IPV]**."
            )
            st.info(
                "**Indicador de Ponto de Virada (IPV)**: Segundo o dicionário de dados, é a métrica de Média das Notas de Ponto de Virada do Aluno. A sua coleta se dá por meio de questionários individualizados por aluno e preenchidos por pedagogos e professores.",
                icon=":material/help:",
            )

        super().__init__(tab)

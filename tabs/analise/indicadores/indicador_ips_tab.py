from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab
from util.layout import format_number
from util.storage import storage_singleton
import streamlit as st


class AnaliseIndicadorIPSTab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IPS"

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

        self.comentario_1_2020 = f"""Começando a análise com o ano de **:blue[2020]**, podemos observar que a grande maioria das notas atribuidos ficou na faixa de **:blue[7,5]**, o que representa um valor aceitável para o aspecto analisado por este indicador."""

        self.comentario_2_2020 = f"""Acima, temos o boxplot a o gráfico de dispersão das observações a respeito do indicador. Podemos observar que de fato, boa parte das notas observadas ficam na faixa de **:blue[7,5]**, com um outro agrupamento logo abaixo, na faixa entre **:blue[6]** e **:blue[7]**. Além disso, também é possível notar que houveram poucos notas acima do **:blue[7,5]**, o que demonstra que apenas os alunos que realmente se sobresairam em tal aspecto receberam uma nota mais alta. Na questão da análise descritiva, temos o seguinte: média em **:blue[{mean_2020}]**, mediana em **:blue[{median_2020}]**, Q1 em **:blue[{q1_2020}]** e Q3 em **:blue[{q3_2020}]**."""

        self.comentario_1_2021 = f"""Para **:blue[2021]**, temos uma distribuição muito parecida com **:blue[2020]**, com um leve aumento na quantidade de notas atribuidas na faixa de **:blue[7,5]**, portanto, entendemos que o desempenho geral deste indicador foi maior que se comparado ao ano anterior."""

        self.comentario_2_2021 = f"""O boxplot do ano de **:blue[2021]** ajuda a corroborar a afirmação anterior, onde podemos observar uma "caixa" pequena no boxplot, o que demonstra uma variação pequena nos valores observados. Neste ano temos a média em **:blue[{mean_2021}]**, a mediana em **:blue[{median_2021}]** e os intervalos interquartílicos Q1 em **:blue[{q1_2021}]** e Q3 em **:blue[{q3_2021}]**. Assim, é notável que a mediana ficaria próxima de **:blue[7,5]**, devido à quantidade observações e também devido à mediana não ser influenciada por outliers. Já a média (que considera o conjunto como um todo e é influenciada por outliers), teve um valor ligeiramente menor."""

        self.comentario_1_2022 = f"""Para o último ano da análise, podemos observar que o padrão da distribuição se manteve constante se comparado aos outros anos analisados. Foram observados um leve aumento na quantidade de notas no valor **:blue[7]** e **:blue[8]**, mas ainda assim, temos a mediana em torno de **:blue[{median_2022}]**."""

        diff = format_number(desc_2022.loc["mean"] - desc_2021.loc["mean"], "%0.2f")
        self.comentario_2_2022 = f"""Por fim, temos o boxplot junto das observações da distribuição para **:blue[2022]**. Para a análise descritiva temos os seguintes valores: média em **:blue[{mean_2022}]**, mediana em **:blue[{median_2022}]**, Q1 em **:blue[{q1_2022}]** e Q3 em **:blue[{q3_2022}]**. A mediana foi idêntica aos anos anteriores, mas a média foi levemente superior, em cerca de **:blue[{diff}]**, se comparado com o ano de **:blue[2021]**."""

        self.comentario_1_comparacao = f"""Nos gráficos acima, temos os histogramas cumulativos com 2 visões distintas. No primeiro gráfico podemos observar que os 3 anos analisados tem a sua grande maioria de notas atribuídas a partir da faixa de **:blue[7]** e **:blue[7,5]**, fato o qual já foi discutido anteriormente na análise ano a ano. No segundo gráfico temos uma outra observação interessante, onde a maior parte das notas dentro da faixa entre **:blue[0]** e **:blue[2]** são exclusivas do ano de **:blue[2021]**, o que demonstra possivelmente impactos da pandemia de COVID-19 no aspecto psicosocial dos alunos atendidos pela ONG."""

        self.comentario_2_comparacao = f"""Por fim, temos um comparativo lado a lado, de todos os boxplots analisados ano a ano. Fica evidente a concentração de notas atribuídas em determinadas faixas."""

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IPS]**."
            )
            st.info(
                "**Indicador Psicossocial (IPS)**: Segundo o dicionário de dados, é a métrica de Média das Notas Psicossociais do Aluno.",
                icon=":material/help:",
            )

        super().__init__(tab)

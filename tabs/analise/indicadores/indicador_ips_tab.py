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

        self.comentario_1_2020 = f"""TODO: redigir"""

        self.comentario_2_2020 = f"""TODO: redigir"""

        self.comentario_1_2021 = f"""TODO: redigir"""

        self.comentario_2_2021 = f"""TODO: redigir"""

        self.comentario_1_2022 = f"""TODO: redigir"""

        self.comentario_2_2022 = f"""TODO: redigir"""

        self.comentario_1_comparacao = f"""TODO: redigir"""

        self.comentario_2_comparacao = f"""TODO: redigir"""

        with tab:
            st.markdown(
                "Nesta seção serão discutidos os dados anuais dos alunos considerando o indicador **:blue[IPS]**."
            )
            st.info(
                "**Indicador Psicossocial (IPS)**: Segundo o dicionário de dados, é a métrica de Média das Notas Psicossociais do Aluno.",
                icon=":material/help:",
            )

        super().__init__(tab)

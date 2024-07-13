from tabs.analise.demografico.demografico_idade_tab import AnaliseDemograficoIdadeTab
from tabs.analise.demografico.demografico_instituicao_tab import (
    AnaliseDemograficoInstituicaoTab,
)
from tabs.tab import TabInterface
from util.storage import storage_singleton
import streamlit as st


class AnaliseDemograficosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.df_2020 = storage_singleton.df_2020
        self.df_2021 = storage_singleton.df_2021
        self.df_2022 = storage_singleton.df_2022
        self.df_full = storage_singleton.df_full

        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                Nesta seção, serão analisados dados demográficos dos alunos, dentre eles a idade e as instituições de ensino nas quais eles estudaram e/ou estudam. Esta análise permitirá uma compreensão maior a respeito dos alunos que são atendidos pela **:blue[Passos Mágicos]**.
            """
            )

            tab0, tab1 = st.tabs(tabs=["Idade", "Instituição de ensino"])

            AnaliseDemograficoIdadeTab(tab0)
            AnaliseDemograficoInstituicaoTab(tab1)

            # TODO: (se der tempo) no downloads, tem um Tabelas_panorama.zip com os dados populacionais de embu-guaçu... talvez vale fazer uma analise da regiao? focando tambem no publico jovem que a Passos magicos atende?
            # https://censo2022.ibge.gov.br/panorama/
            # https://qedu.org.br/municipio/3515103-embu-guacu/baixar-dados

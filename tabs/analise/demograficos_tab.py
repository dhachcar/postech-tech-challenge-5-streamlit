import pandas as pd
from tabs.analise.demografico.demografico_idade_tab import AnaliseDemograficoIdadeTab
from tabs.analise.demografico.demografico_instituicao_tab import (
    AnaliseDemograficoInstituicaoTab,
)
from tabs.tab import TabInterface
import streamlit as st


class AnaliseDemograficosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.df_2020 = pd.read_csv("assets/csv/processado_base_2020.csv", sep=";")
        self.df_2021 = pd.read_csv("assets/csv/processado_base_2021.csv", sep=";")
        self.df_2022 = pd.read_csv("assets/csv/processado_base_2022.csv", sep=";")
        self.df_full = pd.read_csv("assets/csv/processado_base_full.csv", sep=";")

        self.render()

    def render(self):
        with self.tab:
            tab0, tab1 = st.tabs(tabs=["Idade", "Instituição de ensino"])

            AnaliseDemograficoIdadeTab(tab0)
            AnaliseDemograficoInstituicaoTab(tab1)

            # TODO: (se der tempo) no downloads, tem um Tabelas_panorama.zip com os dados populacionais de embu-guaçu... talvez vale fazer uma analise da regiao? focando tambem no publico jovem que a Passos magicos atende?
            # https://censo2022.ibge.gov.br/panorama/
            # https://qedu.org.br/municipio/3515103-embu-guacu/baixar-dados



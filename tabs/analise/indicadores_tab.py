import pandas as pd
from tabs.analise.indicadores.indicador_iaa_tab import AnaliseIndicadorIAATab
from tabs.analise.indicadores.indicador_ian_tab import AnaliseIndicadorIANTab
from tabs.analise.indicadores.indicador_ida_tab import AnaliseIndicadorIDATab
from tabs.analise.indicadores.indicador_ieg_tab import AnaliseIndicadorIEGTab
from tabs.analise.indicadores.indicador_inde_tab import AnaliseIndicadorINDETab
from tabs.analise.indicadores.indicador_ipp_tab import AnaliseIndicadorIPPTab
from tabs.analise.indicadores.indicador_ips_tab import AnaliseIndicadorIPSTab
from tabs.analise.indicadores.indicador_ipv_tab import AnaliseIndicadorIPVTab
from tabs.analise.indicadores.pedras_tab import AnalisePedraTab
from tabs.tab import TabInterface
import streamlit as st


class AnaliseIndicadoresTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """ 
                    Nesta página serão apresentados as análises anuais de todos os indicadores utilizados pela **:blue[Passos Mágicos]** para compor o índice **:blue[INDE]** (também incluso na análise).<br/>
                    Além disso, conforme apresentado anteriormente, ao todo são **:blue[7]** indicadores individuais que compõem o índice, dentre eles: **:blue[IAN]**, **:blue[IDA]**, **:blue[IEG]**, **:blue[IAA]**, **:blue[IPS]**, **:blue[IPP]** e **:blue[IPV]**. Eles estão divididos em 3 grupos (ou dimensões) principais, conforme abaixo:
                    1. **:blue[Dimensão acadêmica:]** englobando os indicadores **:blue[IAN]**, **:blue[IDA]** e **:blue[IEG]**;
                    1. **:blue[Dimensão psicossocial:]** englobando os indicadores **:blue[IAA]** e **:blue[IPS]**;
                    1. **:blue[Dimensão psicopedagógica:]** englobando os indicadores **:blue[IPP]** e **:blue[IPV]**;
            """,
                unsafe_allow_html=True,
            )

            tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
                tabs=["Pedra", "INDE", "IAN", "IDA", "IEG", "IAA", "IPS", "IPP", "IPV"]
            )

            # TODO: se der tempo, analisar os indicadores por fase

            AnalisePedraTab(tab0)
            AnaliseIndicadorINDETab(tab1)
            AnaliseIndicadorIANTab(tab2)
            AnaliseIndicadorIDATab(tab3)
            AnaliseIndicadorIEGTab(tab4)
            AnaliseIndicadorIAATab(tab5)
            AnaliseIndicadorIPSTab(tab6)
            AnaliseIndicadorIPPTab(tab7)
            AnaliseIndicadorIPVTab(tab8)

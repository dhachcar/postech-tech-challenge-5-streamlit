import pandas as pd
from tabs.analise.indicadores.indicador_iaa_tab import AnaliseIndicadorIAATab
from tabs.analise.indicadores.indicador_ian_tab import AnaliseIndicadorIANTab
from tabs.analise.indicadores.indicador_ida_tab import AnaliseIndicadorIDATab
from tabs.analise.indicadores.indicador_ieg_tab import AnaliseIndicadorIEGTab
from tabs.analise.indicadores.indicador_inde_tab import AnaliseIndicadorINDETab
from tabs.analise.indicadores.indicador_ipp_tab import AnaliseIndicadorIPPTab
from tabs.analise.indicadores.indicador_ips_tab import AnaliseIndicadorIPSTab
from tabs.analise.indicadores.indicador_ipv_tab import AnaliseIndicadorIPVTab
from tabs.tab import TabInterface
import streamlit as st


class AnaliseIndicadoresTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Indicadores]")

            tab0, tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
                tabs=["INDE", "IAA", "IEG", "IPS", "IDA", "IPP", "IPV", "IAN"]
            )

            AnaliseIndicadorINDETab(tab0)
            AnaliseIndicadorIAATab(tab1)
            AnaliseIndicadorIEGTab(tab2)
            AnaliseIndicadorIPSTab(tab3)
            AnaliseIndicadorIDATab(tab4)
            AnaliseIndicadorIPPTab(tab5)
            AnaliseIndicadorIPVTab(tab6)
            AnaliseIndicadorIANTab(tab7)

from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroXGBoostTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                TODO: fazer... explicar que o XGBOOST foi um modelo de machine learning utilizado em conjunto da rede NLP criada, explicar funcionamento básico
            """
            )

from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroRedeNeuralTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        x = 1
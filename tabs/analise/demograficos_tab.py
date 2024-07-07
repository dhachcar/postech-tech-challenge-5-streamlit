from tabs.tab import TabInterface
import streamlit as st

class AnaliseDemograficosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            x = "TODO: colocar quantidade de alunos, idade media, maior idade, menor idade, um describe do dataset, colocar os graficos de instituicoes tambem por ano + evolucao da idade media dos alunos e quantidade ao longo dos anos"
import pandas as pd

class Storage:
    def __init__(self):
        self.df_2020 = pd.read_csv("assets/csv/processado_base_2020.csv", sep=";")
        self.df_2021 = pd.read_csv("assets/csv/processado_base_2021.csv", sep=";")
        self.df_2022 = pd.read_csv("assets/csv/processado_base_2022.csv", sep=";")
        self.df_full = pd.read_csv("assets/csv/processado_base_full.csv", sep=";")

storage_singleton = Storage()
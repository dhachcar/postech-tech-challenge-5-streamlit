from tabs.analise.indicadores.indicador_tab import AnaliseIndicadorTab


class AnaliseIndicadorIPVTab(AnaliseIndicadorTab):
    def __init__(self, tab):
        self.tab = tab
        self.col = "IPV"
        self.comentario_1_2020 = 'TODO: redigir'
        self.comentario_2_2020 = 'TODO: redigir'
        self.comentario_1_2021 = 'TODO: redigir'
        self.comentario_2_2021 = 'TODO: redigir'
        self.comentario_1_2022 = 'TODO: redigir'
        self.comentario_2_2022 = 'TODO: redigir'

        super().__init__(tab)

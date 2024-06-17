from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroRedeNeuralTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                As Redes Neurais são modelos computacionais inspirados no funcionamento do próprio cérebro humano. Assim como nosso cérebro é composto por neurônios interconectados, uma rede neural é composta por unidades chamadas "neurônios" ou "nós", organizados em camadas. Cada camada recebe dados, realiza cálculos e passa os resultados para a próxima camada. As redes neurais são projetadas para reconhecer padrões e aprender com exemplos, o que as torna muito eficazes em tarefas como reconhecimento de imagem, processamento de linguagem natural e predição de séries temporais.<br/><br/>
                Tais redes necessitam ingerir grandes quantidades de dados onde, através de um processo de treinamento, ajustam seus parâmetros internos para minimizar erros e melhorar a precisão de sua previsões.<br/><br/>
                O treinamento de uma rede neural envolve a utilização de algoritmos como o retropropagação, que ajusta os pesos das conexões entre os neurônios com base nos erros cometidos durante a previsão. À medida que a rede processa mais dados, ela se torna mais precisa em suas previsões. Neste trabalho, utilizaremos redes de tipo CNN e RNN, que serão explicadas nas próximas seções.
            """,
                unsafe_allow_html=True,
            )

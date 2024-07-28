from tabs.tab import TabInterface
import streamlit as st


class IntroMLPTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Sobre]", divider="blue")
            st.markdown(
                """
                Um **:blue[MLP Perceptron (Multilayer Perceptron)]** é um tipo de rede neural artificial usada em aprendizado de máquina para resolver problemas complexos. Imagine um grande grupo de neurônios conectados em camadas: a camada de entrada recebe os dados, as camadas ocultas processam esses dados através de muitas conexões ponderadas, e a camada de saída fornece a resposta final. Cada neurônio funciona como um pequeno decisor que combina suas entradas e decide se "dispara" ou não, semelhante a como nosso cérebro processa informações. Esse processo permite que o **:blue[MLP]** aprenda padrões e faça previsões precisas, tornando-o uma ferramenta poderosa para tarefas como reconhecimento de imagem e previsão de séries temporais.
            """,
                unsafe_allow_html=True,
            )

            st.subheader(":blue[Aplicação no projeto]", divider="blue")
            st.markdown(
                """Neste projeto, utilizamos um **:blue[MLP]** para identificar se um aluno atendido pela **:blue[Passos Mágicos]** deve ou não receber uma bolsa de estudos. A vantagem aqui está no fato que não precisamos necessariamente fazer um *feature engineering* muito complexo, pois a rede é capaz de identificar padrões por si só. Ainda assim, fazemos alguns tratamentos prévios para facilitar o processo como um todo."""
            )

            st.image(
                "assets/imgs/mlp.jpg",
                caption="Esquema de um MLP Perceptron. Fonte: https://www.geeksforgeeks.org/multi-layer-perceptron-learning-in-tensorflow/",
                width=640,
            )

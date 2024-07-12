from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroSVMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                O **:blue[SVM]** é um tipo de modelo de aprendizado de máquina usada principalmente para classificação. Imagine que você tem uma coleção de pontos em um espaço bidimensional, cada um pertencendo a uma de duas categorias. O **:blue[SVM]** tenta encontrar a melhor linha (ou hiperplano em dimensões mais altas) que separa essas duas categorias com a maior margem possível, ou seja, a linha que deixa a maior distância entre os pontos mais próximos de cada categoria. Essa abordagem ajuda a garantir que o modelo não apenas classifique corretamente os pontos conhecidos, mas também generalize bem para novos pontos.
            """
            )

            st.subheader(":blue[Aplicação no projeto]")

            st.markdown("""TODO: redigir - utilizado junto do NLP""")

            st.image(
                "assets/imgs/svm.png",
                caption="Esquema do modelo SVM. Fonte: scikit-learn (https://scikit-learn.org/stable/modules/svm.html)",
                width=640
            )

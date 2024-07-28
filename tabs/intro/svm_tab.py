from tabs.tab import TabInterface
import streamlit as st


class IntroSVMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Sobre]", divider="blue")
            st.markdown(
                """
                O **:blue[SVM]** é um tipo de modelo de aprendizado de máquina usada principalmente para classificação. Imagine que você tem uma coleção de pontos em um espaço bidimensional, cada um pertencendo a uma de duas categorias. O **:blue[SVM]** tenta encontrar a melhor linha (ou hiperplano em dimensões mais altas) que separa essas duas categorias com a maior margem possível, ou seja, a linha que deixa a maior distância entre os pontos mais próximos de cada categoria. Essa abordagem ajuda a garantir que o modelo não apenas classifique corretamente os pontos conhecidos, mas também generalize bem para novos pontos.<br/><br/>
                Para este projeto especificamente, será utilizado um tipo espécifico de **:blue[SVM]**, no caso o **:blue[SVC (Support Vector Classifier)]** da biblioteca scikit-learn.
            """,
                unsafe_allow_html=True,
            )

            st.subheader(":blue[Aplicação no projeto]", divider="blue")
            st.markdown(
                """No projeto, utilizamos o modelo **:blue[SVC]** em conjunto com o **:blue[NLP]** para categorizar os sentimentos dos textos. Primeiro, o **:blue[NLP]** processa e interpreta os dados, extraindo nuances e características emocionais dos comentários, reviews e tweets. Esses resultados servem de base para o **:blue[SVC]**, que então analisa os padrões nos dados processados e classifica os sentimentos como positivos, negativos ou neutros. Essa integração permite uma análise de sentimentos mais precisa e eficiente, aproveitando a riqueza das informações linguísticas para melhorar a performance do classificador."""
            )

            st.image(
                "assets/imgs/svm.png",
                caption="Esquema do modelo SVM. Fonte: scikit-learn (https://scikit-learn.org/stable/modules/svm.html)",
                width=640,
            )

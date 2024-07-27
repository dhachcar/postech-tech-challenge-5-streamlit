from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroMLPTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Sobre]", divider="blue")
            st.markdown(
                """
                TODO: redigir
                O **:blue[LSTM (Long Short-Term Memory)]** é um tipo especial de **:blue[Rede Neural Recorrente (RNN)]** (discutida na seção anterior) usada para entender padrões em sequências de dados, como textos ou séries temporais. Ela é especialmente boa em capturar dependências a longo prazo, sem ter perdas notavéis de performance como acontece em **:blue[RNNs]** mais simples. Ela já foi amplamente utilizada em outras Tech Challenges apresentados durante o curso :wink:.
            """,
                unsafe_allow_html=True,
            )

            st.subheader(":blue[Aplicação no projeto]", divider="blue")
            st.markdown("""TODO: redigir - utilizado para prever quais alunos podem ser indicados para receber uma bolsa de estudos com uma LSTM (que é uma rnn)... talvez dê p utilizar outro tipo de rede""")

            st.image(
                "assets/imgs/lstm.png",
                caption="Esquema de uma Rede LSTM. Fonte: https://www.deeplearningbook.com.br/as-10-principais-arquiteturas-de-redes-neurais/",
                width=640
            )

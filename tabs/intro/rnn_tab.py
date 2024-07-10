from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroRNNTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                Uma **:blue[Rede Neural Recorrente]** ou **:blue[RNN]** é um tipo de rede neural projetada para processar dados sequenciais, como texto, áudio ou séries temporais. Diferentemente das redes neurais tradicionais, as **:blue[RNNs]** possuem conexões recorrentes que permitem manter e utilizar informações de passos anteriores da sequência, conferindo-lhes uma espécie de memória. Essa característica torna as **:blue[RNNs]** particularmente eficazes em tarefas onde o contexto e a ordem dos dados são cruciais, como tradução automática, reconhecimento de fala e análise de sentimentos. No entanto, **:blue[RNNs]** podem enfrentar dificuldades com dependências de longo prazo, um problema que é mitigado por variantes como o **:blue[LSTM (Long Short-Term Memory)]**, que melhora a capacidade de capturar e manter informações contextuais ao longo de sequências extensas.
            """
            )

            st.subheader(':blue[Aplicação no projeto]')

            st.markdown("""TODO: redigir""")

            st.image(
                "assets/imgs/rnn.jpg",
                caption="Esquema de uma Rede Neural Recorrente (RNN). Fonte: Data Science Academy (https://www.deeplearningbook.com.br/as-10-principais-arquiteturas-de-redes-neurais/)",
                width=480
            )

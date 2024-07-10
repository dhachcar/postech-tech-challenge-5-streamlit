from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroLSTMTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                O **:blue[LSTM]** (Long Short-Term Memory) é um tipo especial de rede neural usada para entender padrões em sequências de dados, como textos ou séries temporais. Ela é capaz de lembrar informações importantes por mais tempo, o que a torna eficaz em tarefas como tradução de idiomas e previsão do tempo.
                Uma rede **:blue[LSTM]** é um tipo especial de rede neural projetada para lidar com dados sequenciais e lembrar informações por longos períodos. Pense nela como um bloco de construção inteligente que pode reter e esquecer informações conforme necessário. Isso a torna ideal para tarefas como prever a próxima palavra em uma frase, traduzir idiomas ou analisar séries temporais, como preços de ações ao longo do tempo. Ela é especialmente boa em capturar dependências a longo prazo, onde eventos passados distantes podem influenciar os resultados futuros. Ela já foi amplatamente utilizada em outras Tech Challenges apresentados durante o curso :wink:.
            """,
                unsafe_allow_html=True,
            )

            st.subheader(":blue[Aplicação no projeto]")

            st.markdown("""TODO: redigir""")

            st.image(
                "assets/imgs/lstm.png",
                caption="Esquema de uma Rede LSTM. Fonte: https://www.deeplearningbook.com.br/as-10-principais-arquiteturas-de-redes-neurais/",
                width=640
            )

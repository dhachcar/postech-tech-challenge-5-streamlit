from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroNLPTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                As redes neurais também são comumente aplicadas ao processamento de linguagem natural **:blue[(NLP)]**. Aqui, elas são modelos computacionais projetados para entender, interpretar e gerar linguagem humana. Elas são treinadas com grandes volumes de texto para reconhecer padrões linguísticos e contextos. Utilizando arquiteturas como redes neurais recorrentes (RNNs) e transformadores, essas redes podem realizar tarefas complexas como tradução automática, análise de sentimentos, resumo de textos e respostas a perguntas. A capacidade das redes neurais de captar nuances e relações contextuais permite que máquinas compreendam e produzam linguagem de maneira mais natural e precisa. Hoje em dia existem grandes players no mercado que lançaram modelos **:blue[NLP]** que são extremamente robustos e aptos a agregar valor no cotidiano da sociedade (OpenAI com o ChatGPT e Google com o Gemini).
            """,
                unsafe_allow_html=True,
            )

            st.subheader(':blue[Aplicação no projeto]')

            st.markdown('''TODO: redigir
                        ''')

            st.image('assets/imgs/nlp.jpg', caption='O que é NLP, fonte: https://amazinum.com/insights/what-is-nlp-and-how-it-is-implemented-in-our-lives/')

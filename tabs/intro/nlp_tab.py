from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroNLPTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Sobre]", divider="blue")
            st.markdown(
                """
                As redes neurais também são comumente aplicadas ao processamento de linguagem natural **:blue[(NLP)]**. Aqui, elas são modelos computacionais projetados para entender, interpretar e gerar linguagem humana. Elas são treinadas com grandes volumes de texto para reconhecer padrões linguísticos e contextos. Utilizando arquiteturas como redes neurais recorrentes **:blue[(RNNs)]** e transformadores, essas redes podem realizar tarefas complexas como tradução automática, análise de sentimentos, resumo de textos e respostas a perguntas. A capacidade das redes neurais de captar nuances e relações contextuais permite que máquinas compreendam e produzam linguagem de maneira mais natural e precisa. Hoje em dia existem grandes players no mercado que lançaram modelos **:blue[NLP]** que são extremamente robustos e aptos a agregar valor no cotidiano da sociedade ( **:blue[OpenAI]** com o  **:blue[ChatGPT]** e  **:blue[Google]** com o  **:blue[Gemini]**).
            """,
                unsafe_allow_html=True,
            )

            st.subheader(":blue[Aplicação no projeto]", divider="blue")
            st.markdown(
                """No projeto, o **:blue[NLP]** é usado para classificar os sentimentos dos comentários e reviews coletados principalmente na página do Facebook da **:blue[Passos Mágicos]**. Para aprimorar a precisão da classificação, o modelo também é treinado com dados adicionais de outras fontes, como tweets e textos gerados artificialmente. Posteriormente, os dados processados pelo **:blue[NLP]** são enviados para um modelo **:blue[SVM]** (mais especificamente o **:blue[SVC]**) para classificação de sentimentos."""
            )

            st.image(
                "assets/imgs/nlp.jpg",
                caption="Esquema de um NLP. Fonte: https://amazinum.com/insights/what-is-nlp-and-how-it-is-implemented-in-our-lives/",
                width=640,
            )

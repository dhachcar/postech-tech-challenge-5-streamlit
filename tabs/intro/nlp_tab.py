from tabs.tab import TabInterface
import streamlit as st


class IntroNLPTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                As redes neurais desempenham um papel fundamental no processamento de linguagem natural **:blue[(NLP)]**, atuando como modelos computacionais projetados para compreender, interpretar e gerar linguagem humana. Elas são treinadas com vastos volumes de texto para identificar padrões e contextos linguísticos. Utilizando arquiteturas avançadas como redes neurais recorrentes **:blue[(RNNs)]** e transformadores, essas redes conseguem realizar tarefas complexas, como tradução automática, análise de sentimentos, resumo de textos e respostas a perguntas. Graças à capacidade de capturar nuances e relações contextuais, as redes neurais permitem que máquinas entendam e produzam linguagem de forma mais natural e precisa. Hoje, grandes players do mercado, como a **:blue[OpenAI]** com o **:blue[ChatGPT]** e o **:blue[Google]** com o **:blue[Gemini]**, lançaram modelos de **:blue[NLP]** extremamente robustos, capazes de agregar valor significativo ao cotidiano da sociedade.
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

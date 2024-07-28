import streamlit as st
from tabs.modelos_e_redes_neurais.analise_sentimento_imagem_tab import (
    ModelosAnaliseSentimentoImagemTab,
)
from tabs.modelos_e_redes_neurais.analise_sentimento_texto_tab import (
    ModelosAnaliseSentimentoTextoTab,
)
from tabs.modelos_e_redes_neurais.previsao_indicacao_bolsa_tab import (
    ModelosPrevisaoIndicacaoBolsaTab,
)
from tabs.modelos_e_redes_neurais.previsao_ponto_virada_tab import (
    ModelosPrevisaoPontoViradaTab,
)
from util.constantes import TITULO_MODELO_E_REDES_NEURAIS, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_MODELO_E_REDES_NEURAIS} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_MODELO_E_REDES_NEURAIS}]")
    st.markdown(
        """
            Abaixo são apresentados os quatro modelos ou redes neurais desenvolvidos para o projeto:
            1. **:blue[Rede Neural MLP (Perceptron Multicamadas)]**: Este modelo é projetado para sugerir bolsas de estudos aos alunos;
            2. **:blue[Modelo XGBoost]**: O objetivo deste modelo é identificar o ponto de virada dos alunos, momento crucial durante a trajetória da pessoa dentro da **:blue[Passos Mágicos]**;
            3. **:blue[Rede Neural de Análise de Sentimento em Imagens]**: Este modelo é treinado em avaliar sentimentos expressos em imagens, sendo utilizado principalmente com as imagens coletadas da página do Facebook da ONG;
            4. **:blue[NLP com SVC (Support Vector Classifier)]**: O quarto e último modelo combina técnicas de **:blue[NLP]** com um classificador **:blue[SVC]** para analisar sentimentos em textos. Este modelo também utiliza dados coletados da página do Facebook da **:blue[Passos Mágicos]** para categorizar os sentimentos expressos nos comentários e reviews;
    """,
        unsafe_allow_html=True,
    )

    tab0, tab1, tab2, tab3 = st.tabs(
        tabs=[
            ":one: Sugestão de indicação de bolsas",
            ":two: Previsão de ponto de virada dos alunos",
            ":three: Análise de sentimentos: Imagem",
            ":four: Análise de sentimentos: Texto",
        ]
    )

    ModelosPrevisaoIndicacaoBolsaTab(tab0)
    ModelosPrevisaoPontoViradaTab(tab1)
    ModelosAnaliseSentimentoImagemTab(tab2)
    ModelosAnaliseSentimentoTextoTab(tab3)

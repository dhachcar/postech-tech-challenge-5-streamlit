import streamlit as st
from tabs.intro.cnn_tab import IntroCNNTab
from tabs.intro.mlp_tab import IntroMLPTab
from tabs.intro.nlp_tab import IntroNLPTab
from tabs.intro.rede_neural_tab import IntroRedeNeuralTab
from tabs.intro.rnn_tab import IntroRNNTab
from tabs.intro.svm_tab import IntroSVMTab
from tabs.intro.xgboost_tab import IntroXGBoostTab
from util.constantes import TITULO_INTRODUCAO, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_INTRODUCAO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_INTRODUCAO}]")

    st.markdown(
        """
        Nas próximas seções, vamos explorar conceitos e tecnologias fundamentais que ajudarão a entender o trabalho realizado. Falaremos sobre tópicos como **:blue[Redes Neurais]**, **:blue[Processamento de Linguagem Natural (NLP)]**, **:blue[Redes Neurais Convolucionais (CNNs)]**, **:blue[Redes Neurais Recorrentes (RNNs)]**, **:blue[Redes Long Short-term Memory (LSTM)]** e alguns modelos de **:blue[Machine Learning]**.
    """
    )

    st.markdown(
        "<small>Para **:blue[navegar entre as abas]**, posicione o mouse em cima das abas e segure a tecla **:blue[[SHIFT]]** e utilize botão central de scroll do mouse :three_button_mouse:</small>",
        unsafe_allow_html=True,
    )

    tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        tabs=[
            "Redes Neurais",
            "Processamento de Linguagem Natural (NLP)",
            "Redes Neurais Convolucionais (CNN)",
            "Redes Neurais Recorrentes (RNN)",
            "Multilayer Perceptron (MLP)",
            "SVM",
            "XGBoost",
        ]
    )

    IntroRedeNeuralTab(tab0)
    IntroNLPTab(tab1)
    IntroCNNTab(tab2)
    IntroRNNTab(tab3)
    IntroMLPTab(tab4)
    IntroSVMTab(tab5)
    IntroXGBoostTab(tab6)

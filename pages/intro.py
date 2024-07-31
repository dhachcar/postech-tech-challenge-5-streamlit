import streamlit as st
from tabs.intro.cnn_tab import IntroCNNTab
from tabs.intro.mlp_tab import IntroMLPTab
from tabs.intro.nlp_tab import IntroNLPTab
from tabs.intro.rede_neural_tab import IntroRedeNeuralTab
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
        Nesta primeira página, iremos explorar alguns conceitos e tecnologias fundamentais que ajudarão a entender o trabalho realizado. Falaremos de forma breve, a respeito de tópicos como **:blue[Redes Neurais]**, **:blue[Processamento de Linguagem Natural (NLP)]**, **:blue[Redes Neurais Convolucionais (CNNs)]**, **:blue[Perceptrons Multilayer (MLPs)]** e alguns modelos de **:blue[Machine Learning]**, dentre eles o **:blue[SVC]** e o **:blue[XGB]**.
    """
    )

    tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(
        tabs=[
            "Redes Neurais",
            "Processamento de Linguagem Natural (NLP)",
            "Redes Neurais Convolucionais (CNN)",
            "Multilayer Perceptron (MLP)",
            "SVM / SVC",
            "XGBoost",
        ]
    )

    IntroRedeNeuralTab(tab0)
    IntroNLPTab(tab1)
    IntroCNNTab(tab2)
    IntroMLPTab(tab3)
    IntroSVMTab(tab4)
    IntroXGBoostTab(tab5)

import streamlit as st
from util.constantes import TITULO_PRINCIPAL, TITULO_REFERENCIAS
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_REFERENCIAS} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_REFERENCIAS}]")

    st.markdown(
        """
        1. Accuracy and Loss. 2020. Disponível em: https://machine-learning.paperspace.com/wiki/accuracy-and-loss. Acesso em: 25/07/2024.
        2. ALVES, I. N. Lemmatization vs. stemming: quando usar cada uma? Alura. 2021. Disponível em: https://www.alura.com.br/artigos/lemmatization-vs-stemming-quando-usar-cada-uma. Acesso em: 20/06/2024.
        3. AUGUSTO. Portuguese Tweets for Sentiment Analysis. Kaggle. 2018. Disponível em: https://www.kaggle.com/datasets/augustop/portuguese-tweets-for-sentiment-analysis/data. Acesso em: 15/07/2024.
        4. BROWNLEE, J. How to Build Multi-Layer Perceptron Neural Network Models with Keras. 2022. Disponível em: https://machinelearningmastery.com/build-multi-layer-perceptron-neural-network-models-keras/. Acesso em: 16/07/2024.
        5. Capítulo 10 – As 10 Principais Arquiteturas de Redes Neurais. Disponível em: https://www.deeplearningbook.com.br/as-10-principais-arquiteturas-de-redes-neurais/. Acesso em: 15/07/2024.
        6. CUNHA, L. S. da. Assimetria e Curtose. Universidade Estadual de Londrina. 2017. Disponível em: https://www.uel.br/pessoal/lscunha/pages/arquivos/uel/Economia%20Noturno/Aula%206%20-%20Assimetria%20e%20Curtose(1).pdf. Acesso em: 02/07/2024.
        7. DEEPAK, R, et al. How to reduce the val_loss and increase val_Accuracy. Kaggle. 2021. Disponível em: https://www.kaggle.com/discussions/questions-and-answers/279139. Acesso em: 05/07/2024.
        8. DRAPALA, J. Kernel Density Estimator explained step by step. Medium. 2023. Disponível em: https://towardsdatascience.com/kernel-density-estimation-explained-step-by-step-7cc5b5bc4517. Acesso em: 27/06/2024.
        9. GOMES, P. C. T. XGBoost: conheça este algoritmo de machine learning. 2019. Disponível em: https://www.datageeks.com.br/xgboost/. Acesso em: 27/06/2024.
        10. Introduction to Convolution Neural Network. 2024. Disponível em: https://www.geeksforgeeks.org/introduction-convolution-neural-network/. Acesso em 30/06/2024.
        11. LASKY, A. Implement Multilayer Perceptron (MLP) with Keras using Fashion MNIST. Medium. 2022. Disponível em: https://medium.com/@artjovianprojects/deep-learning-project-multilayer-perceptron-e34017941918. Acesso em: 16/07/2024.
        12. MOREIRA, S. Rede Neural Perceptron Multicamadas. Medium. 2018. Disponível em: https://medium.com/ensina-ai/rede-neural-perceptron-multicamadas-f9de8471f1a9. Acesso em: 16/07/2024.
        13. Multi-Layer Perceptron Learning in Tensorflow. 2021. Disponível em: https://www.geeksforgeeks.org/multi-layer-perceptron-learning-in-tensorflow/. Acesso em: 18/07/2024.
        14. Naive Bayes vs. SVM for Text Classification. 2024. Disponível em: https://www.geeksforgeeks.org/naive-bayes-vs-svm-for-text-classification/. Acesso em: 09/07/2024.
        15. ONU Brasil - Objetivos de Desenvolvimento Sustentável (ODS). Disponível em: https://brasil.un.org/pt-br/sdgs. Acesso em: 12/06/2024.
        16. ONU - The 17 goals (The Global Goals). Disponível em: https://www.globalgoals.org/goals/. Acesso em: 16/06/2024.
        17. ONU - About Us. Disponível em: https://www.un.org/en/about-us. Acesso em: 16/06/2024.
        18. Passos Mágicos. Disponível em: https://passosmagicos.org.br/ Acesso em: 12/06/2024.
        19. PINHEIRO, N. M. Introdução ao Processamento de Linguagem Natural — Natural Language Processing(NLP). Medium. 2021. Disponível em: https://medium.com/data-hackers/introdu%C3%A7%C3%A3o-ao-processamento-de-linguagem-natural-natural-language-processing-nlp-be907cd06c71. Acesso em: 04/07/2024.
        20. Plotly. Disponível em: https://plotly.com/python. Acesso em: 23/04/2024.
        21. POLONI, K. Redes neurais convolucionais. Medium. 2022. Disponível em: https://medium.com/itau-data/redes-neurais-convolucionais-2206a089c715. Acesso em: 19/06/2024.
        22. RAQUEL, A. Python Journey Machine & Deep Learning. FIAP SHIFT. São Paulo, p.1-101. 2024.
        23. SANDLER, et al. MobileNetV2. Disponível em: https://paperswithcode.com/method/mobilenetv2. Acesso em: 20/06/2024.
        24. SANDLER, et al. MobileNetV2: Inverted Residuals and Linear Bottlenecks. Disponível em: https://paperswithcode.com/paper/mobilenetv2-inverted-residuals-and-linear. Acesso em: 20/06/2024.
        25. SciKit-Learn. Support Vector Machines docs. Disponível em: https://scikit-learn.org/stable/modules/svm.html. Acesso em: 27/06/2024.
        26. SEGATTO, V. SVM, ou Support Vector Machine. Medium. 2023. Disponível em: https://medium.com/liga-mackenzie-de-ia-ci%C3%AAncia-de-dados/svm-ou-support-vector-machine-7efcabdcc7be. Acesso em: 27/06/2024.
        27. SILVA, Dario Rodrigues da. Pesquisa do Desenvolvimento Educacional - PEDE 2020. Associação Passos Mágicos. São Paulo, p.1-108. 2021.
        28. SILVA, Dario Rodrigues da. Pesquisa do Desenvolvimento Educacional - PEDE 2021. Associação Passos Mágicos. São Paulo, p.1-108. 2022.
        29. SILVA, Dario Rodrigues da. Pesquisa do Desenvolvimento Educacional - PEDE 2022. Associação Passos Mágicos. São Paulo, p.1-220. 2023.
        30. SIQUEIRA, D. Histograma: O que é, Exemplos, Gráficos e Tipos. Alura. 2023. Disponível em: https://www.alura.com.br/artigos/o-que-e-um-histograma. Acesso em: 07/07/2024.
        31. Streamlit. API Referente. Disponível em: https://docs.streamlit.io/develop/api-reference. Acesso em: 15/06/2024.
        32. TABOGA, M. Probability density function. Disponível em: https://www.statlect.com/glossary/probability-density-function. Acesso em: 10/07/2024.
        33. What are convolutional neural networks? IBM. Disponível em: https://www.ibm.com/topics/convolutional-neural-networks. Acesso em 28/06/2024.
        34. What is NLP and how It is Implemented in Our Lives. Amazinum. Disponível em: https://amazinum.com/insights/what-is-nlp-and-how-it-is-implemented-in-our-lives/. Acesso em: 19/06/2024.
        35. Wikipedia. ONU. Disponível em: https://pt.wikipedia.org/wiki/Organiza%C3%A7%C3%A3o_das_Na%C3%A7%C3%B5es_Unidas. Acesso em: 16/06/2024.
    """
    )

import streamlit as st
from util.constantes import TITULO_PRINCIPAL, TITULO_TECHCHALLENGE
from util.layout import output_layout
import warnings
import locale


warnings.filterwarnings("ignore")
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
st.set_page_config(
    page_title=TITULO_PRINCIPAL, layout="wide", page_icon="assets/imgs/favicon.ico"
)
output_layout()

_, col0, _ = st.columns([1, 1, 1])

with col0:
    st.header(f":orange[{TITULO_TECHCHALLENGE}]")

st.markdown("#")

_, col0, col1, _ = st.columns([1, 1, 1, 1])

with col0:
    st.image("assets/imgs/logo-fiap.png")

with col1:
    st.image("assets/imgs/logo-postech.png", width=270)

st.markdown("#")

st.subheader(
    ":blue[**:blue[Passos Mágicos]**: o impacto positivo de uma ONG na sociedade]",
    divider="blue",
)
st.markdown(
    """
    A análise de dados tem se tornado uma ferramenta essencial para organizações que buscam compreender e maximizar seu impacto social. No contexto das ONGs, a aplicação de técnicas avançadas de análise, como machine learning e redes neurais, pode proporcionar insights valiosos sobre a eficácia de suas iniciativas. Este trabalho de pós-graduação se propõe a explorar o uso dessas tecnologias na ONG **:blue[Passos Mágicos]**, uma entidade dedicada a promover a inclusão social e o desenvolvimento comunitário por meio de atividades educacionais e culturais.
"""
)

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
    O objetivo deste trabalho é desenvolver um sistema inovador de métricas que revele e ilustre o impacto transformador que a ONG **:blue[Passos Mágicos]** tem na vida das comunidades que atende. Destinado aos alunos da **:blue[PósTech em Data Analytics]**, este desafio é uma oportunidade única de aplicar conhecimentos em **:blue[Análise e Visualização de Dados]**, **:blue[Machine Learning]**, **:blue[Big Data]**, **:blue[Deploy em Produção]**, **:blue[Deep Learning]** e **:blue[Processamento de Linguagem Natural (NLP)]**. A proposta é analisar dados históricos e atuais para compreender as tendências no desenvolvimento educacional e pessoal das crianças e jovens atendidos pela ONG, identificar os fatores-chave que contribuem para o sucesso dessas iniciativas, e desenvolver soluções práticas e sustentáveis que possam ser incorporadas ao dia a dia da ONG.<br/><br/>
    Mais do que números e gráficos, este trabalho visa capturar a essência do impacto emocional e social das atividades da **:blue[Passos Mágicos]**. Utilizando técnicas avançadas de deep learning e **:blue[NLP]**, queremos dar voz aos relatos e feedbacks dos beneficiários, oferecendo uma perspectiva mais profunda e humana sobre os resultados alcançados. Além disso, ao produzir visualizações de dados impactantes, queremos contar a história do trabalho da ONG de uma forma envolvente e compreensível, promovendo transparência e aumentando a conscientização pública sobre a importância dessas iniciativas. Este projeto não só permitirá que os alunos apliquem suas habilidades técnicas em um contexto real, mas também contribuirá significativamente para o aprimoramento das estratégias e operações futuras da ONG, ajudando a transformar ainda mais vidas.
""",
    unsafe_allow_html=True,
)

st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
    A metodologia deste projeto será estruturada em **:blue[4]** etapas, cada uma focada em diferentes aspectos da análise de dados e desenvolvimento de algoritmos de machine learning e redes neurais. Buscamos fornecer uma visão detalhada do impacto emocional e social da ONG **:blue[Passos Mágicos]**, utilizando dados coletados de sua página no Facebook (imagens, comentários, reviews) e dados previamente fornecidos pelos professores.
    1. **:blue[Análise Exploratória de Dados:]** Nesta etapa inicial, coletaremos e prepararemos dados históricos e atuais fornecidos pela ONG **:blue[Passos Mágicos]**, incluindo reviews, comentários e imagens da página do Facebook. Realizaremos uma análise exploratória para identificar padrões e tendências, utilizando ferramentas de visualização para entender a distribuição dos dados e detectar possíveis anomalias.
    2. **:blue[Machine Learning e Redes Neurais:]** Desenvolveremos algoritmos de machine learning para classificar sentimentos nos reviews e comentários da página do Facebook. Estes modelos serão treinados e validados com os feedbacks e anotações a respeito dos alunos, fornecidos pelo dataset disponibilizado pela **:blue[Passos Mágicos]**. Utilizaremos redes neurais convolucionais **:blue[(CNNs)]** para classificação de sentimentos em imagens, identificando expressões faciais e contextos emocionais nas fotos. Redes do tipo **:blue[Perceptron Multilayer (MLP)]** serão empregadas para sugerir a concessão de bolsas de estudo. Além disso, usaremos o **:blue[SVC]** para classificação de sentimento com **:blue[NLP]** e o **:blue[XGB]** para previsão de ponto de virada dos alunos.
    3. **:blue[NLP:]** Aplicaremos técnicas de **:blue[Processamento de Linguagem Natural (NLP)]** para analisar os sentimentos expressos em textos. Isso permitirá uma compreensão mais profunda das emoções e percepções dos beneficiários e da comunidade em relação às atividades da ONG.
    4. **:blue[Conclusão:]** Ao final é feito um fechamento com tudo que foi construído e apresentado durante o decorrer deste trabalho. Além disso, são discutidos os possivéis próximos passos em relação aos modelos e sistemas propostos.
""",
    unsafe_allow_html=True,
)

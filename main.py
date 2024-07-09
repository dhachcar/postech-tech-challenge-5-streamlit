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
    ":blue[Passos Mágicos: o impacto positivo de uma ONG na sociedade]",
    divider="blue",
)
st.markdown(
    """
    A análise de dados tem se tornado uma ferramenta essencial para organizações que buscam compreender e maximizar seu impacto social. No contexto das ONGs, a aplicação de técnicas avançadas de análise, como machine learning e redes neurais, pode proporcionar insights valiosos sobre a eficácia de suas iniciativas. Este trabalho de pós-graduação se propõe a explorar o uso dessas tecnologias na ONG Passos Mágicos, uma entidade dedicada a promover a inclusão social e o desenvolvimento comunitário por meio de atividades educacionais e culturais.
"""
)

st.subheader(":blue[Objetivo]", divider="blue")
st.markdown(
    """
    O objetivo deste trabalho é desenvolver um sistema inovador de métricas que revele e ilustre o impacto transformador que a ONG Passos Mágicos tem na vida das comunidades que atende. Destinado aos alunos da PósTech em Data Analytics, este desafio é uma oportunidade única de aplicar conhecimentos em Análise e Visualização de Dados, Machine Learning, Big Data, Deploy em Produção, Deep Learning e Processamento de Linguagem Natural (NLP). A proposta é analisar dados históricos e atuais para compreender as tendências no desenvolvimento educacional e pessoal das crianças e jovens atendidos pela ONG, identificar os fatores-chave que contribuem para o sucesso dessas iniciativas, e desenvolver soluções práticas e sustentáveis que possam ser incorporadas ao dia a dia da ONG.<br/><br/>
    Mais do que números e gráficos, este trabalho visa capturar a essência do impacto emocional e social das atividades da Passos Mágicos. Utilizando técnicas avançadas de deep learning e NLP, queremos dar voz aos relatos e feedbacks dos beneficiários, oferecendo uma perspectiva mais profunda e humana sobre os resultados alcançados. Além disso, ao produzir visualizações de dados impactantes, queremos contar a história do trabalho da ONG de uma forma envolvente e compreensível, promovendo transparência e aumentando a conscientização pública sobre a importância dessas iniciativas. Este projeto não só permitirá que os alunos apliquem suas habilidades técnicas em um contexto real, mas também contribuirá significativamente para o aprimoramento das estratégias e operações futuras da ONG, ajudando a transformar ainda mais vidas.
""",
    unsafe_allow_html=True,
)

st.subheader(":blue[Metodologia]", divider="blue")
st.markdown(
    """
    A metodologia deste projeto será estruturada em 4 etapas, cada uma focada em diferentes aspectos da análise de dados e desenvolvimento de algoritmos de machine learning e redes neurais. Buscamos fornecer uma visão detalhada do impacto emocional e social da ONG Passos Mágicos, utilizando dados coletados de sua página no Facebook (imagens, comentários, reviews) e dados previamente fornecidos pelos professores.
    1. Análise Exploratória de Dados: Nesta etapa inicial, coletaremos e prepararemos dados históricos e atuais fornecidos pela ONG Passos Mágicos, incluindo reviews, comentários e imagens da página do Facebook. Realizaremos uma análise exploratória para identificar padrões e tendências, utilizando ferramentas de visualização para entender a distribuição dos dados e detectar possíveis anomalias.
    2. Machine Learning e Redes Neurais: Desenvolveremos algoritmos de machine learning para classificar sentimentos nos reviews e comentários da página do Facebook. Utilizaremos redes neurais convolucionais (CNNs) para analisar sentimentos em imagens, identificando expressões faciais e contextos emocionais nas fotos. Os modelos serão treinados e validados para garantir precisão e eficácia.
    3. Machine Learning e NLP: Aplicaremos técnicas de Processamento de Linguagem Natural (NLP) utilizando redes neurais recorrentes (RNNs) e transformers para analisar os sentimentos expressos em textos. Isso permitirá uma compreensão mais profunda das emoções e percepções dos beneficiários e da comunidade em relação às atividades da ONG.
    4. Conclusão: Os resultados das análises serão integrados em um sistema prático e eficiente, com ferramentas de visualização de dados que apresentem os insights de forma clara e impactante. Este sistema ajudará a ONG Passos Mágicos a tomar decisões informadas, melhorar suas estratégias e comunicar seu impacto de maneira eficaz.
""",
    unsafe_allow_html=True,
)

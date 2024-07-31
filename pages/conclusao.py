import streamlit as st
from util.constantes import TITULO_CONCLUSAO, TITULO_PRINCIPAL
from util.layout import output_layout

st.set_page_config(
    page_title=f"{TITULO_CONCLUSAO} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_CONCLUSAO}]")

st.markdown(
    """
    Ao longo deste trabalho, foram desenvolvidos e aplicados uma variedade de modelos de machine learning para explorar e implementar soluções para a ONG **:blue[Passos Mágicos]**. Utilizamos **:blue[CNNs]** para classificar sentimentos em imagens, identificando expressões faciais e contextos emocionais. Redes **:blue[Perceptron Multilayer (MLP)]** foram empregadas para sugerir concessão de bolsas de estudo, enquanto modelos **:blue[SVC]** analisaram sentimentos em texto usando **:blue[NLP]**, e o **:blue[XGB]** ajudou a prever pontos de virada no desempenho dos alunos. Esses modelos mostraram-se eficazes o bastante, a ponto de proporcionar insights valiosos e suporte à tomada de decisões.<br/><br/>
    Para aumentar a robustez e a performance, os modelos criados poderiam ser disponibilizados através de uma plataforma na nuvem. Essa abordagem permitiria um processamento mais eficiente e escalável dos dados, além de facilitar a integração com outras fontes de informação. Com isso, poderíamos extrair insights ainda mais valiosos e abrangentes, potencializando o impacto das ações da ONG e otimizando a tomada de decisões estratégicas. Para esta entrega em especial, isso acabou ficando de fora do escopo do projeto (principalmente pelos custos que isso envolveria), mas com certeza seria aplicável num cenário de uso real.<br/><br/>
    Agora com o futuro em foco, propomos melhorias contínuas nos processos de treinamento e validação dos modelos, garantindo uma precisão ainda maior. Além disso, a criação de um sistema robusto de métricas automatizadas poderia acompanhar o progresso dos alunos de forma contínua, prevendo automaticamente reconhecimentos e prêmios baseados no desempenho, como a concessão de bolsas de estudo. Esse desenvolvimento tornaria o acompanhamento do impacto das ações da ONG mais dinâmico e preciso, beneficiando diretamente os alunos e a comunidade atendida, além de também agilizar a automatizar sistemas de recompensa baseados em performance (no caso da bolsa de estudos).
""",
    unsafe_allow_html=True,
)

st.subheader(":blue[Encerramento e agradecimentos]", divider="blue")
st.markdown(
    """
    Assim concluo este projeto e o meu curso de pós-graduação na FIAP em Data Analytics. Gostaria de aproveitar o momento para expressar a minha profunda e mais sincera gratidão aos professores **:blue[Ana Raquel]**, **:blue[Matheus Pavani]**, **:blue[Edgard Kiriyama]** e, mais recentemente, ao professor **:blue[William]**, por todas as aulas ministradas e o conteúdo compartilhado. Com seus conhecimentos na área de Data Science, tive a oportunidade de explorar um mundo o qual era totalmente novo para mim, já que tenho um background mais forte em desenvolvimento. Tenho certeza que levarei todos os aprendizados deste curso para o resto de minha carreira & vida. Saio muito satisfeito com tudo o que aprendi. Agradeço a todos pelo suporte e dedicação. Muito obrigado e nos vemos por ai!<br/><br/>
    *:orange[Danilo Henrique Achcar]*
""",
    unsafe_allow_html=True,
)

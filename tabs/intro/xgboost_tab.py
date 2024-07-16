from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class IntroXGBoostTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                O **:blue[XGBoost]**, (também conhecido como eXtreme Gradient Boosting), é um algoritmo avançado de aprendizado de máquina que se destaca por sua eficiência e precisão em tarefas de classificação e regressão. Ele é baseado em árvores de decisão, mas utiliza uma técnica chamada "boosting" para aumentar o desempenho. Em vez de criar uma única árvore de decisão complexa, o **:blue[XGBoost]** constrói várias árvores simples e as combina de forma inteligente. Cada nova árvore é criada para corrigir os erros das árvores anteriores, o que melhora gradualmente a precisão do modelo.<br/>
                Um dos segredos do **:blue[XGBoost]** é como ele lida com os erros. A cada passo, ele dá mais peso aos exemplos que foram mal classificados nas árvores anteriores, garantindo que o modelo aprenda com seus próprios erros. Além disso, o **:blue[XGBoost]** incorpora técnicas avançadas como regularização, que ajuda a evitar o overfitting (quando o modelo se ajusta demais aos dados de treinamento e não generaliza bem para novos dados). Ele também utiliza uma abordagem paralela para o treinamento das árvores, o que o torna muito rápido, mesmo em grandes volumes de dados. Por essas razões, o **:blue[XGBoost]** é uma ferramenta poderosa e popular entre cientistas de dados e engenheiros de machine learning.
            """,
                unsafe_allow_html=True,
            )

            st.subheader(":blue[Aplicação no projeto]")

            st.markdown("""TODO: redigir - utilizar NLP para avaliar as descriçoes dos alunos e prever com base nos comentarios se o aluno vai atingir o PV (ponto de virada)""")

            st.image(
                "assets/imgs/xgboost.webp",
                caption="Esquema do XGBoost. Fonte: DataGeeks (https://www.datageeks.com.br/xgboost/)",
                width=860
            )

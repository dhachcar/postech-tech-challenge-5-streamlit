from tabs.tab import TabInterface
import streamlit as st


class IntroXGBoostTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                O **:blue[XGBoost]**, (também conhecido como **:blue[eXtreme Gradient Boosting]** ou **:blue[XGB]**), é um algoritmo avançado de aprendizado de máquina que se destaca por sua eficiência e precisão em tarefas de classificação e regressão. Ele é baseado em árvores de decisão, mas utiliza uma técnica chamada "boosting" para aumentar o desempenho. Em vez de criar uma única árvore de decisão complexa, o **:blue[XGBoost]** constrói várias árvores simples e as combina de forma inteligente. Cada nova árvore é criada para corrigir os erros das árvores anteriores, o que melhora gradualmente a precisão do modelo.<br/><br/>
                Uma das vantagens do **:blue[XGBoost]** é como ele lida com os erros. A cada passo, ele dá mais peso aos exemplos que foram mal classificados nas árvores anteriores, garantindo que o modelo aprenda com seus próprios erros. Além disso, o **:blue[XGBoost]** incorpora técnicas avançadas como regularização, que ajuda a evitar o *overfitting* (quando o modelo se ajusta demais aos dados de treinamento e não generaliza bem para novos dados). Ele também utiliza uma abordagem paralela para o treinamento das árvores, o que o torna muito rápido, mesmo em grandes volumes de dados. Por essas razões, o **:blue[XGBoost]** é uma ferramenta poderosa e popular entre cientistas de dados e engenheiros de machine learning.
            """,
                unsafe_allow_html=True,
            )

            st.subheader(":blue[Aplicação no projeto]", divider="blue")
            st.markdown(
                """O **:blue[XGB]** é utilizado no projeto para prever o ponto de virada dos alunos, processando dados que incluem indicadores de performance e comentários fornecidos pelos professores. Esses comentários são previamente tratados por um sistema de **:blue[NLP]** que os categoriza como positivos, neutros ou negativos. Com todos esses dados em mãos, o **:blue[XGB]** fornece sua previsão final a respeito ponto de virada dos alunos."""
            )

            st.image(
                "assets/imgs/xgboost.webp",
                caption="Esquema do XGBoost. Fonte: DataGeeks (https://www.datageeks.com.br/xgboost/)",
                width=860,
            )

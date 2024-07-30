from tabs.tab import TabInterface
import streamlit as st


class ModelosPrevisaoPontoViradaSobreTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                f"""
                A proposta deste modelo é identificar o ponto de virada de um aluno dentro da **:blue[Passos Mágicos]**, utilizando como base alguns comentários de destaque que os próprios professores alimentam na base de dados, juntamente com seus indicadores de performance. Esse ponto de virada representa um momento crucial na jornada de aprendizado do estudante, onde mudanças significativas em seu desempenho são observadas. Para isso, analisamos detalhadamente os feedbacks fornecidos pelos professores e correlacionamos esses insights com métricas de desempenho dos alunos, como notas, participação em sala e outros indicadores relevantes.<br/><br/>
                Os comentários dados pelos professores são então classificados por um sistema de **:blue[NLP]**, que os categoriza como positivos, neutros ou negativos. Esses dados categorizados, juntamente com os indicadores de performance, são alimentados em um modelo **:blue[XGB]**. Este modelo avançado de machine learning é responsável por fazer a previsão do ponto de virada do aluno
                """,
                unsafe_allow_html=True,
            )

            st.info(
                "**IMPORTANTE**: Foram criados 2 versões do **NLP** para este projeto. Os detalhes de ambas serão discutidos na seção de **\"Análise de sentimento: Texto\"**. De maneira resumida, para a análise dos comentários que serão utilizados pelo **XGB**, optou-se por utilizar a **V2** que é melhor em identificar comentários positivos ou negativos, em detrimento da identificação de comentários neutros.",
                icon=":material/help:",
            )
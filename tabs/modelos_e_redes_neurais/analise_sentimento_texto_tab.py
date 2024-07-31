import joblib
from tabs.tab import TabInterface
import streamlit as st
from util.constantes import (
    CLASS_PREDICT_TEXT_NEGATIVO,
    CLASS_PREDICT_TEXT_NEUTRO,
    CLASS_PREDICT_TEXT_POSITIVO,
)
from util.layout import format_number
from util.nlp_utils import tokenizer


class ModelosAnaliseSentimentoTextoTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def predict(self, texto):
        texto_tokenizado = tokenizer(texto)
        text_vect = self.vect.transform([texto_tokenizado])
        pred = self.modelo.predict(text_vect)

        if pred == CLASS_PREDICT_TEXT_POSITIVO:
            st.success(
                ":white_check_mark: Classificação sugerida: **Positivo** :grinning:"
            )
        elif pred == CLASS_PREDICT_TEXT_NEUTRO:
            st.warning(":warning: Classificação sugerida: **Neutro** :neutral_face:")
        elif pred == CLASS_PREDICT_TEXT_NEGATIVO:
            st.error(":x: Classificação sugerida: **Negativo** :angry:")
        else:
            st.error(":x: Ocorre um erro durante a classificação.")

    def render(self):
        with self.tab:
            st.markdown(
                """
                O **:blue[NLP]** do projeto é treinado utilizando dados de comentários e reviews da página do Facebook da **:blue[Passos Mágicos]**, aproveitando a vasta quantidade de interações autênticas e diversificadas dos usuários. Esses dados refletem uma ampla gama de opiniões e sentimentos reais, proporcionando uma base robusta para o treinamento do modelo.<br/><br/>
                Além dos dados do Facebook, o **:blue[NLP]** do projeto também se beneficia de dados gerados pelo **:blue[ChatGPT]** da **:blue[OpenAI]**, que ajudam a complementar e diversificar o conjunto de treinamento. A geração de dados sintéticos pelo **:blue[ChatGPT]** pode preencher lacunas onde os dados reais são escassos ou desbalanceados<br/><br/>
                Para completar o treinamento, o **:blue[NLP]** do projeto utiliza um conjunto de dados do **:blue[Kaggle]**, especificamente do repositório **:blue["augustop/portuguese-tweets-for-sentiment-analysis"]**. Esse dataset oferece uma rica coleção de tweets em português, rotulados para análise de sentimento, adicionando uma dimensão valiosa de dados anotados manualmente. Com a integração desses dados, o **:blue[NLP]** do projeto não só se beneficia de exemplos diversificados em termos de formato e origem, mas também de dados de alta qualidade e bem rotulados, essenciais para melhorar a precisão e a confiabilidade das previsões de sentimento e outras tarefas relacionadas à **:blue[NLP]**.
            """,
                unsafe_allow_html=True,
            )

            st.link_button(
                "Repositório Kaggle",
                "https://www.kaggle.com/datasets/augustop/portuguese-tweets-for-sentiment-analysis",
            )

            st.subheader(
                ":blue[Categorizando os resultados do NLP com o modelo SVC]",
                divider="blue",
            )
            st.markdown(
                """
                O resultado do **:blue[NLP]** do projeto serve de base para o **:blue[SVC]** utilizado pelo projeto categorizar os sentimentos dos textos. Depois que o **:blue[NLP]** processa e interpreta os dados, extraindo nuances e características emocionais dos comentários, reviews e tweets, essas informações são repassadas para o **:blue[SVC]**.<br/><br/>
                O **:blue[SVC]**, então, usa esses dados para identificar padrões e categorizar o sentimento de cada texto como positivo, negativo ou neutro. Essa integração permite uma análise de sentimentos mais precisa e eficiente, aproveitando a riqueza dos dados linguísticos processados pelo **:blue[NLP]** para melhorar a performance do classificador.<br/><br/>
                Com isso, foram criadas **:blue[2 versões]** do modelo **:blue[NLP]** com **:blue[SVC]**. A **:blue[1ª versão]** parece ser melhor em identificar mensagens com conteúdo mais neutro, enquanto que a **:blue[2ª versão]** aparenta se sobressair em relação à V1 em identificar mensagens positivas ou negativas. À seguir, é possível selecionar a versão desejada do modelo e o texto que deve ser classificado.
            """,
                unsafe_allow_html=True,
            )

            st.divider()

            with st.container():
                col0, col1, col3 = st.columns([2, 2, 8])

                # versão do modelo
                with col0:
                    versoes = {1: "V1", 2: "V2"}
                    versao = st.selectbox(
                        "Versão",
                        key="input_versao",
                        options=list(versoes),
                        format_func=(lambda x: versoes[x]),
                        help="Selecione a versão do modelo NLP",
                    )

                    self.modelo = joblib.load(f"assets/modelos/nlp/v{versao}/model.pkl")
                    self.vect = joblib.load(f"assets/modelos/nlp/v{versao}/vect.pkl")
                    st.success(f":white_check_mark: Modelo V{versao} carregado.")

                with col1:
                    acuracia = format_number(76.81, "%0.2f")
                    st.metric("Acurácia modelo **:orange[V1]**", value=f"{acuracia}%")

                    acuracia = format_number(78.89, "%0.2f")
                    st.metric("Acurácia modelo **:orange[V2]**", value=f"{acuracia}%")

                with col3:
                    txt = st.text_area(
                        "Review/comentário",
                        placeholder="Digite o texto para ser analisado aqui...",
                    )

            if (
                st.button(
                    ":crystal_ball: Classificar sentimento",
                    key="btn_predict_svc",
                )
                and txt
                and txt is not None
            ):
                with st.spinner("Processando..."):
                    self.predict(txt)

            with st.container():
                st.subheader(":blue[Validações pré-configuradas]", divider="blue")
                st.warning(
                    "**IMPORTANTE:** Este NLP foi desenvolvida com uma combinação de dados de treinamento e teste, **:red[podendo apresentar inconsistências em seus resultados]**. Um treinamento mais abrangente está fora do escopo deste projeto. Como sugestão para futuros desenvolvimentos, podemos utilizar um conjunto maior de dados de treinamento para aprimorar o resultado final.",
                    icon=":material/warning:",
                )

                msg = None

                col0, col1, col2 = st.columns(3)

                with col0:
                    text = "Parece uma boa ONG, contudo poderia ser mais transparente!"
                    if st.button(
                        f"**Validação** :one:: {text}", use_container_width=True
                    ):
                        msg = text

                with col1:
                    text = "ONG ótima."
                    if st.button(
                        f"**Validação** :two:: {text}", use_container_width=True
                    ):
                        msg = text

                with col2:
                    text = "Péssimos serviços prestados."
                    if st.button(
                        f"**Validação** :three:: {text}", use_container_width=True
                    ):
                        msg = text

                if msg and msg is not None:
                    self.predict(msg)

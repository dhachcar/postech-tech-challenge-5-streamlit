import time
import unicodedata
import joblib
from tabs.tab import TabInterface
import streamlit as st
import nltk
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


class ModelosAnaliseSentimentoTextoTab(TabInterface):
    def __init__(self, tab):
        nltk.download("stopwords", quiet=True)
        nltk.download("punkt", quiet=True)

        self.tab = tab
        self.modelo = joblib.load("assets/modelos/nlp/model.pkl")
        self.vect = joblib.load("assets/modelos/nlp/vect.pkl")
        self.render()

    def normalize_accents(self, text):
        return (
            unicodedata.normalize("NFKD", text)
            .encode("ASCII", "ignore")
            .decode("utf-8")
        )

    def remove_punctuation(self, text):
        punctuations = string.punctuation
        table = str.maketrans({key: " " for key in punctuations})
        text = text.translate(table)
        return text

    def normalize_str(self, text):
        text = text.lower()
        text = self.remove_punctuation(text)
        text = self.normalize_accents(text)
        text = re.sub(re.compile(r" +"), " ", text)
        return " ".join([w for w in text.split()])

    def tokenizer(self, text):
        stop_words = stopwords.words("portuguese")
        if isinstance(text, str):
            text = self.normalize_str(text)
            text = "".join([w for w in text if not w.isdigit()])
            text = word_tokenize(text)
            text = [x for x in text if x not in stop_words]
            text = [y for y in text if len(y) > 2]
            return " ".join([t for t in text])
        else:
            return None

    def predict(self, texto):
        texto_tokenizado = self.tokenizer(texto)
        text_vect = self.vect.transform([texto_tokenizado])
        pred = self.modelo.predict(text_vect)

        st.markdown(pred)

    def render(self):
        with self.tab:
            st.markdown(
                """
                Uma **:blue[Rede Neural Convolucional]** ou **:blue[CNN]** é um tipo de rede neural especialmente eficaz para processar e analisar dados com uma estrutura matricial, como por exemplo, imagens (que são nada mais que uma matriz de bytes). Inspirada pela organização do córtex visual animal, uma **:blue[CNN]** utiliza camadas de convolução para detectar características locais, como bordas, texturas e padrões, em diferentes níveis de abstração. Essas camadas são seguidas por camadas de pooling que reduzem a dimensionalidade dos dados, mantendo as informações mais relevantes. Esse processo de extração hierárquica de características permite que a **:blue[CNN]** aprenda a reconhecer objetos e padrões visuais de forma altamente eficiente, tornando-a amplamente utilizada em tarefas de visão computacional, como classificação de imagens, detecção de objetos e segmentação semântica.
            """
            )

            txt = st.text_area("Review/comentário")

            # TODO: talvez colocar um botao?

            if txt and txt is not None:
                with st.spinner("Processando..."):
                    time.sleep(3)

                    self.predict(txt)

            # TODO: deixar blocos pre prontos com os resultados e exemplos (utilizar textos/reviews/comentarios da pagina facebook)
            # TODO: colocar o resultado da accuracy_score (mesma função das aulas, verificar qual é)
            # TODO: explicar que foi utilizado ChatGPT para gerar frases para treino, colocar um seção expclicando isso
            # TODO: treinar o modelo tbm com os reviews do dataset!!! e colcoar uma seção explicando isso

            st.markdown(
                """
                **:red[IMPORTANTE:] Esta rede neural foi desenvolvida com um conjunto limitado de dados de treinamento e teste, podendo apresentar inconsistências em seus resultados. Um treinamento mais abrangente está fora do escopo deste projeto. Como sugestão para futuros desenvolvimentos, podemos utilizar um conjunto maior de dados de treinamento para aprimorar o resultado final.**
            """
            )
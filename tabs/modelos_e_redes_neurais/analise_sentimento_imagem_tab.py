import time
from tabs.tab import TabInterface
import streamlit as st
import cv2
import numpy as np
from keras.models import load_model


class ModelosAnaliseSentimentoImagemTab(TabInterface):
    image_size = 256
    categorias = ["feliz", "neutro", "triste", "bravo"]

    def __init__(self, tab):
        self.tab = tab
        self.modelo = load_model("assets/modelos/cnn")
        self.render()

    def predict(self, file_bytes):
        image = cv2.imdecode(file_bytes, 1)
        img = (
            cv2.resize(image, (self.image_size, self.image_size)).astype("float32")
            / 255.0
        )
        img = np.expand_dims(img, axis=0)
        pred = self.modelo.predict(img)
        classes = np.argmax(pred, axis=1)

        # classe prevista
        classe = self.categorias[classes[0]]

        print("Previsões:", pred)
        print("Classe prevista:", classe)

        st.markdown(classe)
        st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    def render(self):
        with self.tab:
            st.markdown(
                """
                Uma **:blue[Rede Neural Convolucional]** ou **:blue[CNN]** é um tipo de rede neural especialmente eficaz para processar e analisar dados com uma estrutura matricial, como por exemplo, imagens (que são nada mais que uma matriz de bytes). Inspirada pela organização do córtex visual animal, uma **:blue[CNN]** utiliza camadas de convolução para detectar características locais, como bordas, texturas e padrões, em diferentes níveis de abstração. Essas camadas são seguidas por camadas de pooling que reduzem a dimensionalidade dos dados, mantendo as informações mais relevantes. Esse processo de extração hierárquica de características permite que a **:blue[CNN]** aprenda a reconhecer objetos e padrões visuais de forma altamente eficiente, tornando-a amplamente utilizada em tarefas de visão computacional, como classificação de imagens, detecção de objetos e segmentação semântica.
            """
            )

            fs = st.file_uploader("upload a file")

            # TODO: talvez colocar um botao?

            if fs is not None:
                with st.spinner("Processando..."):
                    time.sleep(3)

                    file_bytes = np.asarray(bytearray(fs.read()), dtype=np.uint8)
                    self.predict(file_bytes)

            # TODO: deixar blocos pre prontos com os resultados e exemplos (utilizar imgs da pagina facebook)
            # TODO: colocar o resultado da accuracy_score (mesma função das aulas, verificar qual é)
            # TODO: explicar que foi utilizado uma rede concorrente para gerar imagens de treino

            st.markdown(
                """
                **:red[IMPORTANTE:] Esta rede neural foi desenvolvida com um conjunto limitado de dados de treinamento e teste, podendo apresentar inconsistências em seus resultados. Um treinamento mais abrangente está fora do escopo deste projeto. Como sugestão para futuros desenvolvimentos, podemos utilizar um conjunto maior de dados de treinamento para aprimorar o resultado final.**
            """
            )
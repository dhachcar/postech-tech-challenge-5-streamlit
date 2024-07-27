from tabs.tab import TabInterface
from PIL import Image
import io
import streamlit as st
import cv2
import numpy as np
from keras.models import load_model
from util.constantes import (
    CLASS_PREDICT_IMG_NEGATIVO,
    CLASS_PREDICT_IMG_NEUTRO,
    CLASS_PREDICT_IMG_POSITIVO,
)


class ModelosAnaliseSentimentoImagemTab(TabInterface):
    image_size = 256
    categorias = ["feliz", "neutro", "triste", "bravo"]

    def __init__(self, tab):
        self.tab = tab

        self.max_upload_size = 5 * 1024 * 1024  # 5MB

        self.modelo = load_model("assets/modelos/cnn")

        self.render()

    def predict(self, file_bytes, preview=True):
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

        # output da classificação
        if classe == CLASS_PREDICT_IMG_POSITIVO:
            st.success(
                ":white_check_mark: Classificação sugerida: **Feliz** :grinning:"
            )
        elif classe == CLASS_PREDICT_IMG_NEUTRO:
            st.warning(":warning: Classificação sugerida: **Neutro** :neutral_face:")
        elif classe == CLASS_PREDICT_IMG_NEGATIVO:
            st.error(":x: Classificação sugerida: **Bravo** :angry: / **Triste** :disappointed:")
        else:
            st.error(":x: Ocorre um erro durante a classificação.")

        # preview
        if preview:
            st.image(
                cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
                width=250,
                caption="Visualização da imagem enviada",
            )

    def render(self):
        with self.tab:
            st.subheader(
                ":blue[Utilização de uma CNN para análise de sentimentos em imagens]"
            )
            st.markdown(
                """
                Uma **:blue[Rede Neural Convolucional]** ou **:blue[CNN]** é um tipo de rede neural especialmente eficaz para processar e analisar dados com uma estrutura matricial, como por exemplo, imagens (que são nada mais que uma matriz de bytes). Inspirada pela organização do córtex visual animal, uma **:blue[CNN]** utiliza camadas de convolução para detectar características locais, como bordas, texturas e padrões, em diferentes níveis de abstração. Essas camadas são seguidas por camadas de pooling que reduzem a dimensionalidade dos dados, mantendo as informações mais relevantes. Esse processo de extração hierárquica de características permite que a **:blue[CNN]** aprenda a reconhecer objetos e padrões visuais de forma altamente eficiente, tornando-a amplamente utilizada em tarefas de visão computacional, como classificação de imagens, detecção de objetos e segmentação semântica.<br/><br/>
                Aqui também é importante frisar que dado a complexidade e necessidades computacionais para treinamento de um modelo robusto e abrangente do tipo, a rede neural aqui apresentada utiliza um modelo base em sua criação, no caso o **:blue[MobileNetV2]**. Isso visa encurtar o caminho para a criação de um modelo MVP que permita analisar as imagens das pessoas impactadas pela ONG **:blue[Passos Mágicos]**.
            """,
                unsafe_allow_html=True,
            )

            st.divider()

            fs = st.file_uploader(
                "Enviar imagem para análise",
                type=["jpg", "png"],
                help="Por limitação do Streamlit, a validação de tamanho é feita posteriormente. **:blue[Máximo = 5MB]**",
            )

            if (
                st.button(
                    ":crystal_ball: Classificar sentimento",
                    key="btn_predict_cnn",
                )
                and fs
                and fs is not None
            ):
                with st.spinner("Processando..."):
                    file_size = fs.size

                    if file_size > self.max_upload_size:
                        st.error(
                            f"O arquivo é muito grande. O tamanho máximo permitido é {self.max_upload_size}MB."
                        )
                    else:
                        st.success(
                            f":white_check_mark: **Arquivo carregado com sucesso:** {fs.name}"
                        )

                        file_bytes = np.asarray(bytearray(fs.read()), dtype=np.uint8)
                        self.predict(file_bytes)

            with st.container():
                st.subheader(":blue[Validações pré-configuradas]", divider="blue")
                to_predict = None

                col0, col1, col2, col3, col4, col5, col6, col7 = st.columns(8)
                width = 150

                with col0:
                    image = "assets/modelos/cnn/exemplos/1.jpg"

                    if st.button(":crystal_ball: Classificar", key="btn_cnn_predict_1"):
                        to_predict = image

                    st.image(image, width=width, caption="Exemplo 1")

                with col1:
                    image = "assets/modelos/cnn/exemplos/2.jpg"

                    if st.button(":crystal_ball: Classificar", key="btn_cnn_predict_2"):
                        to_predict = image

                    st.image(image, width=width, caption="Exemplo 2")

                with col2:
                    image = "assets/modelos/cnn/exemplos/3.jpg"

                    if st.button(":crystal_ball: Classificar", key="btn_cnn_predict_3"):
                        to_predict = image

                    st.image(image, width=width, caption="Exemplo 3")

                with col3:
                    image = "assets/modelos/cnn/exemplos/4.png"

                    if st.button(":crystal_ball: Classificar", key="btn_cnn_predict_4"):
                        to_predict = image

                    st.image(image, width=width, caption="Exemplo 4")

                with col4:
                    image = "assets/modelos/cnn/exemplos/5.png"

                    if st.button(":crystal_ball: Classificar", key="btn_cnn_predict_5"):
                        to_predict = image

                    st.image(image, width=width, caption="Exemplo 5")

                with col5:
                    image = "assets/modelos/cnn/exemplos/6.png"

                    if st.button(":crystal_ball: Classificar", key="btn_cnn_predict_6"):
                        to_predict = image

                    st.image(image, width=width, caption="Exemplo 6")

                with col6:
                    image = "assets/modelos/cnn/exemplos/7.jpg"

                    if st.button(":crystal_ball: Classificar", key="btn_cnn_predict_7"):
                        to_predict = image

                    st.image(image, width=width, caption="Exemplo 7")

                with col7:
                    image = "assets/modelos/cnn/exemplos/8.jpg"

                    if st.button(":crystal_ball: Classificar", key="btn_cnn_predict_8"):
                        to_predict = image

                    st.image(image, width=width, caption="Exemplo 8")

                if to_predict and to_predict is not None:
                    image = Image.open(to_predict)
                    file_bytes = io.BytesIO()

                    image.save(file_bytes, format=image.format)
                    file_bytes = np.asarray(bytearray(file_bytes.getvalue()))

                    self.predict(file_bytes, preview=False)

            # TODO: colocar mais imagens ... agora usando da paginad o facebook
            # TODO: colocar o resultado da accuracy_score (mesma função das aulas, verificar qual é)
            # TODO: explicar sobre as 3 classes possiveis feliz, neutro, bravo e falar q é possivel expandir
            # TODO: fazer rodar na nuvem

            st.markdown(
                """
                **:red[IMPORTANTE:] Esta rede neural foi desenvolvida com um conjunto limitado de dados de treinamento e teste, podendo apresentar inconsistências em seus resultados. Um treinamento mais abrangente está fora do escopo deste projeto. Como sugestão para futuros desenvolvimentos, podemos utilizar um conjunto maior de dados de treinamento para aprimorar o resultado final.**
            """
            )

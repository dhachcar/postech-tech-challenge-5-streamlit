from tabs.tab import TabInterface
from PIL import Image
import io
import streamlit as st
import cv2
import numpy as np
from keras.models import load_model
from util.constantes import (
    CLASS_PREDICT_IMG_BRAVO,
    CLASS_PREDICT_IMG_TRISTE,
    CLASS_PREDICT_IMG_NEUTRO,
    CLASS_PREDICT_IMG_FELIZ,
)


class ModelosAnaliseSentimentoImagemTab(TabInterface):
    image_size = 224
    classes_previsao = ["feliz", "neutro", "bravo", "triste"]

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
        classe_idx = np.argmax(pred, axis=1)[0]
        classe_pred = self.classes_previsao[classe_idx]

        print("Previsões:", pred)
        print("Index:", classe_idx)
        print("Classe prevista:", classe_pred)

        # output da classificação
        if classe_pred == CLASS_PREDICT_IMG_FELIZ:
            st.success(
                ":white_check_mark: Classificação sugerida: **Feliz** :grinning:"
            )
        elif classe_pred == CLASS_PREDICT_IMG_NEUTRO:
            st.warning(":warning: Classificação sugerida: **Neutro** :neutral_face:")
        elif classe_pred == CLASS_PREDICT_IMG_BRAVO:
            st.error(":x: Classificação sugerida: **Bravo** :angry:")
        elif classe_pred == CLASS_PREDICT_IMG_TRISTE:
            st.error(":x: Classificação sugerida: **Triste** :disappointed:")
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
            st.markdown(
                """
                A **:blue[CNN]** criada para este projeto tem como objetivo classificar imagens da ONG **:blue[Passos Mágicos]**, identificando quatro sentimentos: **:orange[feliz]**, **:orange[neutro]**, **:orange[bravo]** e **:orange[triste]**. Através dessa classificação, a rede neural permite uma análise mais precisa do impacto das ações da ONG na sociedade, fornecendo insights valiosos sobre as reações emocionais dos beneficiários. Além disso, essa abordagem pode ser expandida no futuro para desenvolver um sistema de avaliação de sentimentos mais abrangente, potencializando a capacidade da ONG de medir e aprimorar suas iniciativas com base no feedback emocional da comunidade.<br/><br/>
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
                st.info(
                    "**AVISO**: Algumas das fotos apresentadas abaixo foram retiradas da página pública do Facebook da **Passos Mágicos**. Algumas delas também foram manipuladas para focarem exclusivamente nos rostos das pessoas.",
                    icon=":material/help:",
                )
                st.warning(
                    "**IMPORTANTE:** Esta rede neural foi desenvolvida com um conjunto limitado de dados de treinamento e teste, **:red[podendo apresentar inconsistências em seus resultados]**. Um treinamento mais abrangente está fora do escopo deste projeto. Como sugestão para futuros desenvolvimentos, podemos utilizar um conjunto maior de dados de treinamento para aprimorar o resultado final.",
                    icon=":material/warning:",
                )

                width = 150

                def output_img_for_prediction(img, idx):
                    to_predict = None
                    image = f"assets/modelos/cnn/exemplos/{img}"

                    if st.button(
                        ":crystal_ball: Classificar", key=f"btn_cnn_predict_{idx}"
                    ):
                        to_predict = image

                    st.image(image, width=width, caption=f"Exemplo {idx}")

                    if to_predict and to_predict is not None:
                        image = Image.open(to_predict)
                        file_bytes = io.BytesIO()

                        image.save(file_bytes, format=image.format)
                        file_bytes = np.asarray(bytearray(file_bytes.getvalue()))

                        self.predict(file_bytes, preview=False)

                with st.container():
                    col0, col1, col2, col3, col4, col5 = st.columns(6)

                    with col0:
                        output_img_for_prediction("1.jpg", 1)

                    with col1:
                        output_img_for_prediction("2.jpg", 2)

                    with col2:
                        output_img_for_prediction("3.jpg", 3)

                    with col3:
                        output_img_for_prediction("4.png", 4)

                    with col4:
                        output_img_for_prediction("5.png", 5)

                    with col5:
                        output_img_for_prediction("6.png", 6)

                with st.container():
                    col0, col1, col2, col3, col4, col5 = st.columns(6)

                    with col0:
                        output_img_for_prediction("7.jpg", 7)

                    with col1:
                        output_img_for_prediction("8.jpg", 8)

                    with col2:
                        output_img_for_prediction("9.jpg", 9)

                    with col3:
                        output_img_for_prediction("10.jpg", 10)

                    with col4:
                        output_img_for_prediction("11.jpg", 11)

                    with col5:
                        output_img_for_prediction("12.jpg", 12)

                with st.container():
                    col0, col1, col2, col3, col4, col5 = st.columns(6)

                    with col0:
                        output_img_for_prediction("13.jpg", 13)

                    with col1:
                        output_img_for_prediction("14.jpg", 14)

                    with col2:
                        output_img_for_prediction("15.jpg", 15)

                    with col3:
                        output_img_for_prediction("16.jpg", 16)

                    with col4:
                        output_img_for_prediction("17.jpg", 17)

                    with col5:
                        output_img_for_prediction("18.jpg", 18)

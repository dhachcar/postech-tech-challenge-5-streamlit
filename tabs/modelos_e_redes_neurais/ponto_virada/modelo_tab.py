import pandas as pd
from tabs.tab import TabInterface
import streamlit as st
import joblib


class ModelosPrevisaoPontoViradaModeloTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.modelo = joblib.load("assets/modelos/xgboost/xgb.pkl")
        self.onehotencoder = joblib.load("assets/modelos/xgboost/onehotencoder.pkl")

        self.render()

    def predict(self, aluno):
        x = 1

        # TODO: consumir as funcoes NLP externalizadas
        # df = processar_sentimento_nlp_df(df)
        # df = aplicar_onehot_encoder(df)
        # df = df[sorted(df.columns)]


        pred = self.modelo.predict(aluno)

        # TODO: colcoar st.ballons caso preveja o ponto de virada

        st.write(pred)

    def render(self):
        with self.tab:
            with st.container():
                col0, col1, col2 = st.columns(3)

                with col0:
                    txt_destaque_ieg = st.text_area(
                        "**:blue[Destaque IEG]**",
                        placeholder="Digite o texto de 'Destaque IEG' para ser analisado aqui...",
                    )

                with col1:
                    txt_destaque_ida = st.text_area(
                        "**:blue[Destaque IDA]**",
                        placeholder="Digite o texto de 'Destaque IDA' para ser analisado aqui...",
                    )

                with col2:
                    txt_destaque_ipv = st.text_area(
                        "**:blue[Destaque IPV]**",
                        placeholder="Digite o texto de 'Destaque IPV' para ser analisado aqui...",
                    )

            with st.container():
                col0, col1, col2, col3 = st.columns(4)

                with col0:
                    indicador_inde = st.number_input(
                        label="**:blue[INDE]**",
                        key="xgb_inde",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col1:
                    indicador_ian = st.number_input(
                        label="**:blue[IAN]**",
                        key="xgb_ian",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col2:
                    indicador_ida = st.number_input(
                        label="**:blue[IDA]**",
                        key="xgb_ida",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col3:
                    indicador_ieg = st.number_input(
                        label="**:blue[IEG]**",
                        key="xgb_ieg",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

            with st.container():
                col0, col1, col2, col3 = st.columns(4)

                with col0:
                    indicador_iaa = st.number_input(
                        label="**:blue[IAA]**",
                        key="xgb_iaa",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col1:
                    indicador_ips = st.number_input(
                        label="**:blue[IPS]**",
                        key="xgb_ips",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col2:
                    indicador_ipp = st.number_input(
                        label="**:blue[IPP]**",
                        key="xgb_ipp",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

                with col3:
                    indicador_ipv = st.number_input(
                        label="**:blue[IPV]**",
                        key="xgb_ipv",
                        min_value=0.0,
                        max_value=10.0,
                        value=0.0,
                        step=0.1,
                        format="%.2f",
                    )

            aluno = pd.DataFrame(
                {
                    "DESTAQUE_IEG": txt_destaque_ieg,
                    "DESTAQUE_IDA": txt_destaque_ida,
                    "DESTAQUE_IPV": txt_destaque_ipv,
                    "IAA": indicador_iaa,
                    "IAN": indicador_ian,
                    "IDA": indicador_ida,
                    "IEG": indicador_ieg,
                    "INDE": indicador_inde,
                    "IPP": indicador_ipp,
                    "IPS": indicador_ips,
                    "IPV": indicador_ipv,
                },
                index=[0],
            )

            if st.button(":crystal_ball: Prever", key="btn_predict_xgb"):
                with st.spinner("Processando..."):
                    st.subheader(":blue[Matriz de entrada do modelo]", divider="blue")
                    st.dataframe(aluno, hide_index=True)

                    st.subheader(":blue[Previsão do modelo]", divider="blue")
                    self.predict(aluno)

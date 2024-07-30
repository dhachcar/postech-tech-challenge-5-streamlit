import pandas as pd
from tabs.tab import TabInterface
import streamlit as st
import joblib

from util.nlp_utils import tokenizer


class ModelosPrevisaoPontoViradaModeloTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab

        self.xgb = joblib.load("assets/modelos/xgboost/xgb.pkl")
        self.xgb_onehotencoder = joblib.load("assets/modelos/xgboost/onehotencoder.pkl")
        self.nlp_modelo = joblib.load(f"assets/modelos/nlp/v2/model.pkl")
        self.nlp_vect = joblib.load(f"assets/modelos/nlp/v2/vect.pkl")

        self.render()

    def predict(self, aluno):
        def predict_nlp_sentiment(texto):
            texto_teste = tokenizer(texto)
            text_vect = self.nlp_vect.transform([texto_teste])
            return self.nlp_modelo.predict(text_vect)[0]

        def processar_sentimento_nlp_df(df):
            df["DESTAQUE_IEG_NLP"] = df["DESTAQUE_IEG"].apply(
                lambda x: predict_nlp_sentiment(x) if pd.notnull(x) else "NA"
            )
            df["DESTAQUE_IDA_NLP"] = df["DESTAQUE_IDA"].apply(
                lambda x: predict_nlp_sentiment(x) if pd.notnull(x) else "NA"
            )
            df["DESTAQUE_IPV_NLP"] = df["DESTAQUE_IPV"].apply(
                lambda x: predict_nlp_sentiment(x) if pd.notnull(x) else "NA"
            )
            return df

        def aplicar_onehot_encoder(df):
            # colunas que vão receber o OneHotEncoder
            cols_to_encode = [
                "DESTAQUE_IDA_NLP",
                "DESTAQUE_IEG_NLP",
                "DESTAQUE_IPV_NLP",
            ]
            df[cols_to_encode] = df[cols_to_encode].astype(str)

            # dropa as colunas originais que o NLP processou
            df.drop(
                ["DESTAQUE_IDA", "DESTAQUE_IEG", "DESTAQUE_IPV"], axis=1, inplace=True
            )

            # aplica o OneHotEncoder
            codificado = self.xgb_onehotencoder.fit_transform(df[cols_to_encode])
            colunas_codificadas = self.xgb_onehotencoder.get_feature_names_out(
                cols_to_encode
            )
            df_codificado = pd.DataFrame(codificado, columns=colunas_codificadas)

            # pode ser que um registro não possua todas as colunas finais do OneHotEncoder (p.ex. quando para a coluna IPV não é classificada como neutra),
            # entretanto, o NLP ainda pode eventualmente classificar tal feature como neutra, o que quebraria o modelo em tal caso
            # o código a seguir, garante que todas as linhas do df possuam as variantes geradas pelo NLP
            colunas_necessarias = [
                "DESTAQUE_IDA_NLP_NA",
                "DESTAQUE_IDA_NLP_negativo",
                "DESTAQUE_IDA_NLP_neutro",
                "DESTAQUE_IDA_NLP_positivo",
                "DESTAQUE_IEG_NLP_NA",
                "DESTAQUE_IEG_NLP_negativo",
                "DESTAQUE_IEG_NLP_neutro",
                "DESTAQUE_IEG_NLP_positivo",
                "DESTAQUE_IPV_NLP_NA",
                "DESTAQUE_IPV_NLP_negativo",
                "DESTAQUE_IPV_NLP_neutro",
                "DESTAQUE_IPV_NLP_positivo",
            ]

            for col in colunas_necessarias:
                if col not in df_codificado.columns:
                    df_codificado[col] = 0

            # reseta o index para o concat
            df_codificado = df_codificado.reset_index(drop=True)
            df = df.reset_index(drop=True)

            # concat final das colunas (OneHotEncoder + colunas originais - colunas originais que deveriam ser encodadas)
            df_final = pd.concat(
                [df_codificado, df.drop(columns=cols_to_encode)], axis=1
            )

            return df_final

        # processa os dados
        df = aluno.copy()
        df = processar_sentimento_nlp_df(df)  # roda o NLP em cima dos comentários
        df = aplicar_onehot_encoder(df)  # aplica onehotencoder no resultado do NLP
        df = df[sorted(df.columns)]
        pred = self.xgb.predict(df)

        st.subheader(":blue[Matriz de entrada processada para o modelo]", divider="blue")
        st.dataframe(df, hide_index=True)

        st.subheader(":blue[Previsão do modelo]", divider="blue")
        if pred > 0:
            st.balloons()
            st.success(
                ":white_check_mark: **Previsão:** o aluno **atingiu** seu ponto de virada :grinning:"
            )
        else:
            st.warning(
                ":warning: **Previsão:** o aluno ainda **não atingiu** seu ponto de virada :disappointed:"
            )

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

                    self.predict(aluno)

from tabs.tab import TabInterface
import streamlit as st


class ModelosLstmTab(TabInterface):
    def __init__(self, tab):

        self.tab = tab
        # self.modelo = joblib.load("assets/modelos/nlp/model.pkl")
        # self.vect = joblib.load("assets/modelos/nlp/vect.pkl")
        self.render()

    def predict(self, texto):
        x = 1
        # texto_tokenizado = self.tokenizer(texto)
        # text_vect = self.vect.transform([texto_tokenizado])
        # pred = self.modelo.predict(text_vect)

        # st.markdown(pred)

    def render(self):
        with self.tab:
            x = 1

            st.markdown(
                ":red[TODO: criar modelo LSTM para identificar se um aluno irá atingir ou não seu ponto de virada (IPV)]"
            )

            # TODO: qual a ideia para esse LSTM?

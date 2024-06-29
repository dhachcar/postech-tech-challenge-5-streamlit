from tabs.tab import TabInterface


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
            
            
            # TODO: qual a ideia para esse LSTM?
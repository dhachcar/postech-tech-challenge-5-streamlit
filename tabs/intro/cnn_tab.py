from tabs.tab import TabInterface
import streamlit as st


class IntroCNNTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                Uma **:blue[Rede Neural Convolucional]** ou **:blue[CNN]** é um tipo de rede neural especialmente eficaz para processar e analisar dados com uma estrutura matricial, como por exemplo, imagens (que são nada mais que uma matriz de bytes). Inspirada pela organização do córtex visual animal, uma **:blue[CNN]** utiliza camadas de convolução para detectar características locais, como bordas, texturas e padrões, em diferentes níveis de abstração. Essas camadas são seguidas por camadas de pooling que reduzem a dimensionalidade dos dados, mantendo as informações mais relevantes. Esse processo de extração hierárquica de características permite que a **:blue[CNN]** aprenda a reconhecer objetos e padrões visuais de forma altamente eficiente, tornando-a amplamente utilizada em tarefas de visão computacional, como classificação de imagens, detecção de objetos e segmentação semântica.
            """
            )

            st.subheader(":blue[Aplicação no projeto]", divider="blue")
            st.markdown(
                """Neste projeto, foi criado uma **:blue[CNN]** para analisar o sentimento das imagens encontradas na página do Facebook da **:blue[Passos Mágicos]**. A princípio é apenas uma demonstração do que é possível atingir, mas o modelo poderia eventualmente evoluir para um sistema mais robusto de métricas que consolide o impacto positivo que a ONG tem na vida das pessoas."""
            )

            st.image(
                "assets/imgs/cnn.png",
                caption="Esquema de uma Rede Neural Convolucional (CNN). Fonte: https://medium.com/itau-data/redes-neurais-convolucionais-2206a089c715",
                width=860,
            )

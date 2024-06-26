from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class PassosMagicosBaseDadosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(
                """
                    Base de dados

                    TODO: falar a respeito da base de dados, os dados anonimizados, quantidade de alunos e a relação dela com o dicionário, disponibilizar link de download da base anonimizada e do dicionario
                    
                """,
                unsafe_allow_html=True,
            )

            with st.container():
                col0, col1 = st.columns([1, 1])

                with col0:
                    st.subheader(":blue[Missão]", divider="blue")
                    st.markdown(
                        """
                        Conforme a própria ONG descreve, sua missão é:<br/>
                        ***:orange[(...) transformar a vida de jovens e crianças, oferecendo ferramentas para levá-los a melhores oportunidades de vida.]***
                        """,
                        unsafe_allow_html=True,
                    )

                with col1:
                    st.subheader(":blue[Visão]", divider="blue")
                    st.markdown(
                        """
                        A respeito de sua visão, conforme seu site instituicional, é apresentada como:<br/>
                        ***:orange[(...) viver em um Brasil no qual todas as crianças e jovens têm iguais oportunidades para realizarem seus sonhos e são agentes transformadores de suas próprias vidas.]***
                        """,
                        unsafe_allow_html=True,
                    )

            with st.container():
                st.subheader(":blue[Valores]", divider="blue")
                st.markdown(
                    """
                    - Empatia
                    - Amor ao aprendizado
                    - Poder em acreditar em si e no próximo
                    - Pertencimento
                    - Gratidão
                    - Busca pelo saber
                    - Educação que transforma e ajuda a transformar
                    - Aprender a aprender
                """
                )

            with st.container():
                st.subheader(":blue[Impacto social em 2023]", divider="blue")
                st.markdown(
                    """A seguir, apresentamos alguns indicadores de impacto da ONG, conforme disponibilizados em seu site. Estes indicadores são comparados com os de 2022, permitindo visualizar a evolução nos últimos dois anos."""
                )

                metrica2022_pessoas_impactadas = 0
                metrica2022_alunos_programa = 970
                metrica2022_bolsistas_ensino_particular = 112
                metrica2022_bolsistas_ensino_superior = 71

                metrica2023_pessoas_impactadas = 4400
                metrica2023_alunos_programa = 1100
                metrica2023_bolsistas_ensino_particular = 100
                metrica2023_bolsistas_ensino_superior = 94

                def calc_metrica_comparativa(indicador2022, indicador2023):
                    return format_number(
                        ((indicador2023 * 100) / indicador2022) - 100, "%0.4f"
                    )

                metrica2022x2023_alunos_programa = calc_metrica_comparativa(
                    metrica2022_alunos_programa, metrica2023_alunos_programa
                )
                metrica2022x2023_bolsistas_ensino_particular = calc_metrica_comparativa(
                    metrica2022_bolsistas_ensino_particular,
                    metrica2023_bolsistas_ensino_particular,
                )
                metrica2022x2023_bolsistas_ensino_superior = calc_metrica_comparativa(
                    metrica2022_bolsistas_ensino_superior,
                    metrica2023_bolsistas_ensino_superior,
                )

                _, col0, col1, _ = st.columns([0.5, 1, 1, 0.5])

                with col0:
                    st.metric(
                        label="Pessoas impactadas",
                        value=format_number(metrica2023_pessoas_impactadas),
                        delta="sem dados entre 2022 x 2023",
                        delta_color="off",
                    )

                with col1:
                    st.metric(
                        label="Alunos no programa de Aceleração do conhecimento",
                        value=format_number(metrica2023_alunos_programa),
                        delta=f"{metrica2022x2023_alunos_programa}% em relação à 2022",
                    )

                _, col0, col1, _ = st.columns([0.5, 1, 1, 0.5])

                with col0:
                    st.metric(
                        label="Bolsistas em instituições de ensino particular",
                        value=format_number(metrica2023_bolsistas_ensino_particular),
                        delta=f"{metrica2022x2023_bolsistas_ensino_particular}% em relação à 2022",
                    )

                with col1:
                    st.metric(
                        label="Bolsistas em instituições de ensino superior",
                        value=format_number(metrica2023_bolsistas_ensino_superior),
                        delta=f"{metrica2022x2023_bolsistas_ensino_superior}% em relação à 2022",
                    )

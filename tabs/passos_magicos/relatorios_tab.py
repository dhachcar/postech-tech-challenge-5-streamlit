from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class PassosMagicosPEDERelatoriosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[PEDE]", divider="blue")
            st.markdown(
                """
                    O **:blue[PEDE]** ou **:blue[Pesquisa Extensiva do Desenvolvimento Educacional]** é um estudo produzido pela **:blue[ONG Passos Mágicos]** e abrange uma análise detalhada de diversos aspectos educacionais, incluindo avaliações e indicadores relacionados ao desenvolvimento educacional dos jovens que fazem parte de seu programa de ensino.<br/><br/>
                    Dentro do **:blue[PEDE]**, é apresentado o **:blue[Índice Nacional de Desenvolvimento Educacional (INDE)]** que é utilizado no relatório para medir e avaliar diferentes dimensões do desenvolvimento educacional. Ele é composto por vários indicadores que avaliam aspectos como adequação de nível, desempenho acadêmico, engajamento, autoavaliação, aspectos psicossociais e psicopedagógicos, além de um indicador específico chamado "Indicador do Ponto de Virada".<br/><br/>
                    Tais indicadores estão divididos em 3 dimensões principais, conforme abaixo:
                    1. **:blue[Dimensão acadêmica:]** englobando os indicadores **:blue[IAN]**, **:blue[IDA]** e **:blue[IEG]**;
                    2. **:blue[Dimensão psicossocial:]** englobando os indicadores **:blue[IAA]** e **:blue[IPS]**;
                    3. **:blue[Dimensão psicopedagógica:]** englobando os indicadores **:blue[IPP]** e **:blue[IPV]**;

                    O cálculo do **:blue[INDE]** é realizado através da agregação de diversos indicadores que avaliam diferentes aspectos do desenvolvimento educacional. Cada um desses indicadores possui uma ponderação específica, e juntos eles formam a pontuação geral do índice. A respeito das dimensões e indicadores utilizados no cálculo do **:blue[INDE]**, temos o seguinte:

                    * **:blue[Indicador de Adequação de Nível (IAN):]** Avalia se o aluno está no nível adequado de ensino para sua idade;
                    * **:blue[Indicador de Desempenho Acadêmico (IDA):]** Mede o desempenho acadêmico dos alunos em diversas disciplinas;
                    * **:blue[Indicador de Engajamento (IEG):]** Analisa o nível de engajamento dos alunos nas atividades escolares;
                    * **:blue[Indicador de Autoavaliação (IAA):]** Considera as autoavaliações feitas pelos próprios alunos sobre seu desempenho e desenvolvimento;
                    * **:blue[Indicador Psicossocial (IPS):]** Examina aspectos psicossociais dos alunos, incluindo bem-estar emocional e social;
                    * **:blue[Indicador Psicopedagógico (IPP):]** Foca em aspectos psicopedagógicos que podem influenciar o aprendizado dos alunos;
                    * **:blue[Indicador do Ponto de Virada (IPV):]** Identifica momentos críticos no desenvolvimento educacional dos alunos que podem determinar mudanças significativas em seu percurso acadêmico;
                """,
                unsafe_allow_html=True,
            )

            st.subheader(":blue[Metodologia de cálculo]", divider="blue")
            st.markdown(
                "Para calcular o **:blue[INDE]**, os dados são coletados através de questionários e avaliações aplicadas aos alunos, e os resultados são ponderados de acordo com a importância de cada indicador. Cada indicador contribui para uma pontuação final que é utilizada para determinar o **:blue[INDE]** geral e suas variações (universitário, escolar, etc.)."
            )

            st.subheader(":blue[Relatórios]", divider="blue")
            st.markdown(
                "Até o momento, foram criados **:blue[3 relatórios PEDE]**. O primeiro foi apresentado em 2021 e era referente aos dados de 2020. O segundo foi apresentado em 2022 e tinha como base o ano de 2021. Por fim, o relatório mais recente foi criado em 2023 com o ano base de 2022. À seguir, são apresentados links para download de cada relatório:"
            )

            with open("assets/materiais/relatorio-pede-2020.pdf", "rb") as file:
                btn = st.download_button(
                    label="Relatório PEDE 2020",
                    data=file,
                    file_name="relatorio-pede-2020-techchallenge5-danilo-achcar.pdf",
                    mime="application/pdf",
                )

            with open("assets/materiais/relatorio-pede-2021.pdf", "rb") as file:
                btn = st.download_button(
                    label="Relatório PEDE 2021",
                    data=file,
                    file_name="relatorio-pede-2021-techchallenge5-danilo-achcar.pdf",
                    mime="application/pdf",
                )

            with open("assets/materiais/relatorio-pede-2022.pdf", "rb") as file:
                btn = st.download_button(
                    label="Relatório PEDE 2022",
                    data=file,
                    file_name="relatorio-pede-2022-techchallenge5-danilo-achcar.pdf",
                    mime="application/pdf",
                )

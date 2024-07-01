from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class PassosMagicosPEDERelatoriosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(':red[TODO: revisar texto]')
            st.markdown(':red[TODO: rever layout]')

            st.subheader(':blue[PEDE]')
            st.markdown(
                """
                    O PEDE ou Pesquisa Extensiva do Desenvolvimento Educacional é um estudo produzido pela ONG Passos Mágicos e abrange uma análise detalhada de diversos aspectos educacionais, incluindo avaliações e indicadores relacionados ao desenvolvimento educacional dos jovens que fazem parte de seu programa de ensino.<br/><br/>
                    Dentro do PEDE, é apresentado o Índice Nacional de Desenvolvimento Educacional (INDE) que é utilizado no relatório para medir e avaliar diferentes dimensões do desenvolvimento educacional. Ele é composto por vários indicadores que avaliam aspectos como adequação de nível, desempenho acadêmico, engajamento, autoavaliação, aspectos psicossociais e psicopedagógicos, além de um indicador específico chamado "Indicador do Ponto de Virada".<br/><br/>
                    Tais indicadores estão divididos em 3 dimensões principais:
                    1. Dimensão acadêmica: englobando os indicadores IAN, IDA e IEG;
                    2. Dimensão psicossocial: englobando os indicadores IAA e IPS;
                    3. Dimensão psicopedagógica: englobando os indicadores IPP e IPV;

                    O cálculo do Índice Nacional de Desenvolvimento Educacional (INDE) é realizado através da agregação de diversos indicadores que avaliam diferentes aspectos do desenvolvimento educacional. Cada um desses indicadores possui uma ponderação específica, e juntos eles formam a pontuação geral do INDE. As dimensões e indicadores utilizados no cálculo do INDE são os seguintes:

                    Os indicadores podem ser resumidos da seguinte maneira:
                    * Indicador de Adequação de Nível (IAN): Avalia se o aluno está no nível adequado de ensino para sua idade.
                    * Indicador de Desempenho Acadêmico (IDA): Mede o desempenho acadêmico dos alunos em diversas disciplinas.
                    * Indicador de Engajamento (IEG): Analisa o nível de engajamento dos alunos nas atividades escolares.
                    * Indicador de Autoavaliação (IAA): Considera as autoavaliações feitas pelos próprios alunos sobre seu desempenho e desenvolvimento.
                    * Indicador Psicossocial (IPS): Examina aspectos psicossociais dos alunos, incluindo bem-estar emocional e social.
                    * Indicador Psicopedagógico (IPP): Foca em aspectos psicopedagógicos que podem influenciar o aprendizado dos alunos.
                    * Indicador do Ponto de Virada (IPV): Identifica momentos críticos no desenvolvimento educacional dos alunos que podem determinar mudanças significativas em seu percurso acadêmico.
                """,
                unsafe_allow_html=True,
            )

            st.subheader(':blue[Metodologia de cálculo]')
            st.markdown('Para calcular o INDE, os dados são coletados através de questionários e avaliações aplicadas aos alunos, e os resultados são ponderados de acordo com a importância de cada indicador. Cada indicador contribui para uma pontuação final que é utilizada para determinar o INDE geral e suas variações (universitário, escolar, etc.).')
            
            st.subheader(':blue[Relatórios]')
            st.markdown('Até o momento, foram criados 3 relatórios PEDE. O primeiro foi apresentado em 2021 e era referente aos dados de 2020. O segundo foi apresentado em 2022 e tinha como base o ano de 2021. Por fim, o relatório mais recente foi criado em 2023 com o ano base de 2022. À seguir, são apresentados links para download de cada relatório:')

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
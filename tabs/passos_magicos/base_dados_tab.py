from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class PassosMagicosBaseDadosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.markdown(':red[TODO: rever layout]')
            st.markdown(':red[TODO: rever texto]')

            st.subheader(":blue[Base de dados]")
            st.markdown(
                """
                    O trabalho utiliza uma base de dados disponibilizada pela ONG Passos Mágicos, composta por 1349 linhas e 69 colunas. Esta base de dados oferece uma rica variedade de informações detalhadas, com cada linha representando uma entrada única e cada coluna abrangendo uma característica específica dos dados. É importante destacar que todos os dados dos alunos estão devidamente anonimizados, garantindo a privacidade e a proteção das informações pessoais.<br/><br/>
                    Para facilitar a compreensão e a utilização dessa base de dados, a Passos Mágicos disponibiliza um dicionário de dados para download. Este dicionário de dados serve como um guia essencial, descrevendo de maneira clara e precisa o propósito de cada coluna, os tipos de dados presentes e as possíveis categorias ou valores esperados. Ele é indispensável para analistas, pesquisadores e desenvolvedores que desejam explorar, interpretar e utilizar a base de dados de maneira eficaz e eficiente.<br/><br/>
                    Este recurso não só facilita a navegação e o entendimento dos dados, mas também garante que todos os usuários possam manipular e interpretar as informações de forma consistente e precisa, otimizando a produtividade e a qualidade das análises realizadas.                    
                """,
                unsafe_allow_html=True,
            )

            with open("assets/materiais/dicionario-dados.pdf", "rb") as file:
                btn = st.download_button(
                    label="Dicionários de dados",
                    data=file,
                    file_name="dicionario-dados-techchallenge5-danilo-achcar.pdf",
                    mime="application/pdf",
                )

            with open("assets/csv/dataset_passos_magicos.csv", "rb") as file:
                btn = st.download_button(
                    label="Base de dados anonimizada",
                    data=file,
                    file_name="base-anonimizada-passos-magicos.csv",
                    mime="text/csv",
                )

            st.subheader(":blue[Features utilizadas por este projeto]")

            st.markdown('''
                | Coluna | Descrição |
                |:----------------:|:-------------:|
                | NOME | Nome do Aluno (dados estão anonimizados) |
                | IDADE_ALUNO_2020 | Idade do Aluno em 2020 |
                | ANOS_NA_PM_2020 | Tempo (Em Anos) que o Alunos esta na Passos Mágicos em 2020 |
                | PEDRA_2020 | Classificação do Aluno baseado no nu mero do INDE (2020), o conceito de classificaça o e dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294 |
                | IAA_2020 | Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2020 |
                | IEG_2020 | Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2020 |
                | IPS_2020 | Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2020 |
                | IDA_2020 | Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2020 |
                | IPP_2020 | Indicador Psicopedagógico – Média das Notas Psico Pedagógicas do Aluno em 2020 |
                | IPV_2020 | Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2020 |
                | IAN_2020 | Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2020 |
                | PEDRA_2021 | Classificação do Aluno baseado no nu mero do INDE (2021), o conceito de classificaça o e dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294 |
                | IAA_2021 | Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2021 |
                | IEG_2021 | Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2021 |
                | IPS_2021 | Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2021 |
                | IDA_2021 | Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2021 |
                | IPP_2021 | Indicador Psicopedagógico – Média das Notas Psico Pedagógicas do Aluno em 2021 |
                | IPV_2021 | Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2021 |
                | IAN_2021 | Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2021 |
                | PEDRA_2022 | Classificação do Aluno baseado no nu mero do INDE (2022), o conceito de classificaça o e dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294 |
                | IAA_2022 | Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2022 |
                | IEG_2022 | Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2022 |
                | IPS_2022 | Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2022 |
                | IDA_2022 | Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2022 |
                | IPP_2022 | Indicador Psicopedagógico – Média das Notas Psico Pedagógicas do Aluno em 2022 |
                | IPV_2022 | Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2022 |
                | IAN_2022 | Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2022 |
            ''')
             

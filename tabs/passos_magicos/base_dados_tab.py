from tabs.tab import TabInterface
import streamlit as st

from util.layout import format_number


class PassosMagicosBaseDadosTab(TabInterface):
    def __init__(self, tab):
        self.tab = tab
        self.render()

    def render(self):
        with self.tab:
            st.subheader(":blue[Base de dados]", divider="blue")
            st.markdown(
                """
                    O trabalho utiliza uma base de dados disponibilizada pela **:blue[ONG Passos Mágicos]**, composta por **:blue[1349]** linhas e **:blue[69]** colunas. Esta base de dados oferece uma rica variedade de informações detalhadas, com cada linha representando uma entrada única e cada coluna abrangendo uma característica específica dos dados. É importante destacar que todos os dados dos alunos estão devidamente anonimizados, garantindo a privacidade e a proteção das informações pessoais.<br/><br/>
                    Para facilitar a compreensão e a utilização dessa base de dados, a **:blue[Passos Mágicos]** disponibiliza um dicionário de dados para download. Este dicionário de dados serve como um guia essencial, descrevendo de maneira objetiva o propósito de cada coluna, os tipos de dados presentes e as possíveis categorias ou valores esperados. À seguir, é possível realizar o donwload da base de dados original e do dicionário de dados em sua íntegra:<br/>
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

            with open("assets/csv/original_dataset_passos_magicos.csv", "rb") as file:
                btn = st.download_button(
                    label="Base de dados anonimizada",
                    data=file,
                    file_name="base-anonimizada-passos-magicos.csv",
                    mime="text/csv",
                )

            st.error(
                "**ATENÇÃO:** este trabalho utiliza exclusivamente a base de dados ***V1*** fornecida pela **Passos Mágicos**. Quando a ***V2*** foi disponibilizada, o trabalho já estava em estágios avançados de construção e sua mudança poderia trazer dificuldades para a entrega deste projeto.",
                icon=":material/help:",
            )

            st.subheader(":blue[Features utilizadas por este projeto]", divider="blue")
            st.markdown(
                """
                    À seguir, são apresentadas todas as colunas (ou features) que são utilizadas no decorrer deste trabalho. Tais colunas são utilizadas para a criação de modelos de **:blue[Machine Learning]** e **:blue[Redes Neurais]**. A descrição e explicação de cada coluna foi retirada diretamente do dicionário de dados.
                """,
                unsafe_allow_html=True,
            )

            tag_eda = "**:green[EDA]**"  # análise estatística
            tag_nlp = "**:red[NLP]**"  # NLP
            tag_ml = "**:blue[ML]**"  # machine learning ou redes neurais

            st.subheader(":blue[Legenda]")
            st.markdown(
                f"""
                - {tag_eda}: Coluna utilizada para fins de **:green[Análise Exploratória]**
                - {tag_nlp}: Coluna utilizada para fins de treino / validação / consumo de um **:red[NLP]**
                - {tag_ml}: Coluna utilizada para fins de treino / validação / consumo de **:blue[algoritmos de Machine Learning e/ou Redes Neurais]**
            """
            )

            st.markdown(
                f"""
                | Coluna | Propósito princial | Descrição |
                |:----------------:|:-------------:|:-------------:|
                | INSTITUICAO_ENSINO_ALUNO_2020 | {tag_eda} | Mostra instituiça o de Ensino do Aluno em 2020 |
                | NOME | {tag_eda} | Nome do Aluno (dados estão anonimizados) |
                | IDADE_ALUNO_2020 | {tag_eda} | Idade do Aluno em 2020 |
                | PEDRA_2020 | {tag_eda} | Classificação do Aluno baseado no número do INDE (2020), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294 |
                | IAA_2020 | {tag_eda} / {tag_ml} | Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2020 |
                | IEG_2020 | {tag_eda} / {tag_ml} | Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2020 |
                | IPS_2020 | {tag_eda} / {tag_ml} | Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2020 |
                | IDA_2020 | {tag_eda} / {tag_ml} | Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2020 |
                | IPP_2020 | {tag_eda} / {tag_ml} | Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em 2020 |
                | IPV_2020 | {tag_eda} / {tag_ml} | Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2020 |
                | IAN_2020 | {tag_eda} / {tag_ml} | Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2020 |
                | INDE_2020 | {tag_eda} / {tag_ml} | Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2020.
                | DESTAQUE_IEG_2020 | {tag_nlp} | Observações dos Avaliadores Sobre o Aluno referente ao "Indicador de Engajamento” em 2020 |
                | DESTAQUE_IDA_2020 | {tag_nlp} | Observações dos Avaliadores Sobre o Aluno referente ao “Indicador de Aprendizagem” em 2020 |
                | DESTAQUE_IPV_2020 | {tag_nlp} | Observações dos Avaliadores Sobre o Aluno referente ao “Indicador de Ponto de Virada” em 2020 |
                | PONTO_VIRADA_2020 | {tag_nlp} | Campo do Tipo Booleano que sinaliza se o Aluno atingiu o “Ponto de Virada” em 2020 |
                | PEDRA_2021 | {tag_eda} | Classificação do Aluno baseado no número do INDE (2021), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294 |
                | IAA_2021 | {tag_eda} / {tag_ml} | Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2021 |
                | IEG_2021 | {tag_eda} / {tag_ml} | Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2021 |
                | IPS_2021 | {tag_eda} / {tag_ml} | Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2021 |
                | IDA_2021 | {tag_eda} / {tag_ml} | Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2021 |
                | IPP_2021 | {tag_eda} / {tag_ml} | Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em 2021 |
                | IPV_2021 | {tag_eda} / {tag_ml} | Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2021 |
                | IAN_2021 | {tag_eda} / {tag_ml} | Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2021 |
                | INDE_2021 | {tag_eda} / {tag_ml} | Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2021.
                | REC_EQUIPE_1_2021 | {tag_nlp} | Recomendação: da Equipe de Avalição: 1 em 2021 |
                | REC_EQUIPE_2_2021 | {tag_nlp} | Recomendação: da Equipe de Avalição: 2 em 2021 |
                | REC_EQUIPE_3_2021 | {tag_nlp} | Recomendação: da Equipe de Avalição: 3 em 2021 |
                | REC_EQUIPE_4_2021 | {tag_nlp} | Recomendação: da Equipe de Avalição: 3 em 2021 |
                | REC_PSICO_2021 | {tag_nlp} | Mostra qual a recomendação da equipe de psicologia sobre o Aluno em 2021
                | PONTO_VIRADA_2021 | {tag_ml} | Campo do Tipo Booleano que sinaliza se o Aluno atingiu o “Ponto de Virada” em 2021 |
                | PEDRA_2022 | {tag_eda}| Classificação do Aluno baseado no número do INDE (2022), o conceito de classificação é dado por: Quartzo – 2,405 a 5,506 / Ágata – 5,506 a 6,868 / Ametista – 6,868 a 8,230 / Topázio – 8,230 a 9,294 |
                | IAA_2022 | {tag_eda} / {tag_ml}| Indicador de Auto Avaliação – Média das Notas de Auto Avaliação do Aluno em 2022 |
                | IEG_2022 | {tag_eda} / {tag_ml}| Indicador de Engajamento – Média das Notas de Engajamento do Aluno em 2022 |
                | IPS_2022 | {tag_eda} / {tag_ml}| Indicador Psicossocial – Média das Notas Psicossociais do Aluno em 2022 |
                | IDA_2022 | {tag_eda} / {tag_ml}| Indicador de Aprendizagem - Média das Notas do Indicador de Aprendizagem 2022 |
                | IPP_2022 | {tag_eda} / {tag_ml}| Indicador Psicopedagógico – Média das Notas Psicopedagógicas do Aluno em 2022 |
                | IPV_2022 | {tag_eda} / {tag_ml}| Indicador de Ponto de Virada – Média das Notas de Ponto de Virada do Aluno em 2022 |
                | IAN_2022 | {tag_eda} / {tag_ml}| Indicador de Adequação ao Nível – Média das Notas de Adequação do Aluno ao nível atual em 2022 |
                | INDE_2022 | {tag_eda} / {tag_ml}| Índice do Desenvolvimento Educacional – Métrica de Processo Avaliativo Geral do Aluno, dado pela ponderação dos indicadores: IAN, IDA, IEG, IAA, IPS, IPP e IPV em 2022. |
                | REC_PSICO_2022 | {tag_nlp} | Mostra qual a recomendação da equipe de psicologia sobre o Aluno em 2022 |
                | REC_AVA_1_2022 | {tag_nlp}| Recomendação da Equipe de Avalição 1 em 2022 |
                | REC_AVAL_2_2022 | {tag_nlp}| Recomendação da Equipe de Avalição: 2 em 2022 |
                | REC_AVAL_3_2022 | {tag_nlp}| Recomendação da Equipe de Avalição: 3 em 2022 |
                | REC_AVAL_4_2022 | {tag_nlp}| Recomendação da Equipe de Avalição: 3 em 2022 |
                | DESTAQUE_IEG_2022 | {tag_nlp} | Observações dos Mestres Sobre o Aluno referente ao "Indicador de Engajamento” em 2022 |
                | DESTAQUE_IDA_2022 | {tag_nlp} | Observações dos Mestres Sobre o Aluno referente ao “Indicador de Aprendizagem” em 2022 |
                | DESTAQUE_IPV_2022 | {tag_nlp} | Observações dos Mestres Sobre o Aluno referente ao “Indicador de Ponto de Virada” em 2022 |
                | PONTO_VIRADA_2022 | {tag_ml} | Campo do Tipo Booleano que sinaliza se o Aluno atingiu o “Ponto de Virada” em 2022 |
                | INDICADO_BOLSA_2022 | {tag_ml} | Campo do Tipo Booleano que sinaliza se o Aluno foi indicado para alguma Bolsa no Ano de 2022 |
            """,
                unsafe_allow_html=True,
            )

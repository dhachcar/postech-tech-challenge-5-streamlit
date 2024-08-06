import streamlit as st
from tabs.analise.alunos_tab import AnaliseAlunosTab
from tabs.analise.demograficos_tab import AnaliseDemograficosTab
from tabs.analise.indicadores_tab import AnaliseIndicadoresTab
from util.constantes import TITULO_ANALISE_EXPLORATORIA, TITULO_PRINCIPAL
from util.layout import output_layout, format_number
from util.storage import storage_singleton

st.set_page_config(
    page_title=f"{TITULO_ANALISE_EXPLORATORIA} | {TITULO_PRINCIPAL}",
    layout="wide",
)
output_layout()

with st.container():
    st.header(f":orange[{TITULO_ANALISE_EXPLORATORIA}]")

    total_original = format_number(len(storage_singleton.df_original))
    total_2020 = format_number(len(storage_singleton.df_2020))
    total_2021 = format_number(len(storage_singleton.df_2021))
    total_2022 = format_number(len(storage_singleton.df_2022))

    st.markdown(
        f"""
        Para a análise exploratória, foram utilizados dados dos alunos dos anos de **:blue[2020]**, **:blue[2021]** e **:blue[2022]**. A base de dados inicial possui os dados dos alunos de forma consolidada, com os anos representados em diversas colunas.
        Esta base inicial possui um total de **:blue[{total_original}]** registros. O primeiro passo na análise foi quebrar as colunas dos anos em **:blue['N']** registros de um mesmo aluno, um para cada ano, caso assim fosse necessário. Desta forma, caso um aluno possuísse dados nas colunas de **:blue[2020]** e **:blue[2021]**, ele teria **:blue[2]** registros adicionados ao dataset final.<br/><br/>
        Após a etapa inicial de organização, seguiu-se com limpeza dos dados, removendo registros duplicados e inconsistentes. O número de registros considerados no dataset final difere ligeiramente do original, conforme a seguir:
        * Para **:blue[2020]**, foram considerados um total de **:blue[{total_2020}]** alunos;
        * Para **:blue[2021]**, foram considerados um total de **:blue[{total_2021}]** alunos;
        * Por fim, para **:blue[2022]**, foram considerados um total de **:blue[{total_2022}]** alunos;

        Vale também mencionar um ponto importante das próximas seções, a respeito dos histogramas utilizados. Para todos eles, foram utilizadas as funções de **:blue[probabilidade de densidade]** que representam como os valores de uma variável contínua estão distribuídos. Em vez de contar quantos valores caem em cada intervalo, ela usa uma curva para indicar onde os dados são mais prováveis de aparecer. A altura da curva em qualquer ponto mostra a chance relativa de encontrar um valor perto desse ponto, ajudando a visualizar a distribuição dos dados de forma clara e contínua.
    """,
        unsafe_allow_html=True,
    )

    tab0, tab1, tab2 = st.tabs(
        tabs=["Demografia dos alunos", "Indicadores de performance", "Alunos"]
    )

    AnaliseDemograficosTab(tab0)
    AnaliseIndicadoresTab(tab1)
    AnaliseAlunosTab(tab2)

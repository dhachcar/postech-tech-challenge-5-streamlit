import streamlit as st
from st_pages import show_pages, Page
import locale

from util.constantes import (
    TITULO_ANALISE_EXPLORATORIA,
    TITULO_PASSOS_MAGICOS,
    TITULO_INTRODUCAO,
    TITULO_MODELO_E_REDES_NEURAIS,
    TITULO_REFERENCIAS,
)


def format_number(number, format="%0.0f"):
    return locale.format(format, number, grouping=True)


def output_layout():
    show_pages(
        [
            Page("./main.py", "Tech Challenge 5", ":house:", use_relative_hash=True),
            Page(
                "./pages/intro.py", TITULO_INTRODUCAO, ":books:", use_relative_hash=True
            ),
            Page(
                "./pages/passos_magicos.py",
                TITULO_PASSOS_MAGICOS,
                ":open_book:",
                use_relative_hash=True,
            ),
            Page(
                "./pages/analise.py",
                TITULO_ANALISE_EXPLORATORIA,
                ":memo:",
                use_relative_hash=True,
            ),
            Page(
                "./pages/modelos_e_redes_neurais.py",
                TITULO_MODELO_E_REDES_NEURAIS,
                ":robot_face:",
                use_relative_hash=True,
            ),
            Page(
                "./pages/refs.py",
                TITULO_REFERENCIAS,
                ":globe_with_meridians:",
                use_relative_hash=True,
            ),
        ]
    )

    with st.sidebar:
        st.subheader("Aluno")
        st.text("Danilo Henrique Achcar")
        st.text("RM 351516 | 2DTAT")

        st.divider()

        st.subheader("Instalando as dependências do app")
        st.code(body="python -m venv venv", language="shell")
        st.code(body="source venv/Scripts/activate", language="shell")
        st.code(body="pip install -r requirements.txt", language="shell")

        st.divider()

        st.subheader("Executando localmente")
        st.code(body="streamlit run main.py", language="shell")

        st.divider()

        st.subheader("Repositórios do projeto")
        st.link_button(
            "Repositório Streamlit",
            "https://github.com/dhachcar/postech-tech-challenge-5-streamlit",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )
        st.link_button(
            "Repositório Jupyter Notebook",
            "https://github.com/dhachcar/postech-tech-challenge-5",
            help=None,
            type="secondary",
            disabled=False,
            use_container_width=False,
        )

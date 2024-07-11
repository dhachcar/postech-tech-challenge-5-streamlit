import streamlit as st


def output_pedra_ametista(width=180, caption=False, use_column_width=False):
    st.image(
        "assets/imgs/pedras/ametista.png",
        caption="Amétista. Fonte: https://brasilgemas.com" if caption else None,
        width=width,
        use_column_width=use_column_width
    )


def output_pedra_topazio(width=180, caption=False, use_column_width=False):
    st.image(
        "assets/imgs/pedras/topazio.png",
        caption="Topázio. Fonte: https://brasilgemas.com" if caption else None,
        width=width,
        use_column_width=use_column_width
    )


def output_pedra_quartzo(width=140, caption=False, use_column_width=False):
    st.image(
        "assets/imgs/pedras/quartzo.png",
        caption="Quartzo. Fonte: https://img.freepik.com/" if caption else None,
        width=width,
        use_column_width=use_column_width
    )


def output_pedra_agata(width=140, caption=False, use_column_width=False):
    st.image(
        "assets/imgs/pedras/agata.png",
        caption="Ágata. Fonte: https://www.ciadasgemas.com.br/" if caption else None,
        width=width,
        use_column_width=use_column_width
    )

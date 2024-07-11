from typing import Tuple
import pandas as pd
from scipy.stats import gaussian_kde
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from typing import List


def plot_bar(
    df: pd.DataFrame,
    col: str,
    titulo: str,
    xaxis: str,
    yaxis: str = "Quantidade",
    cores: List[str] = None,
) -> pd.DataFrame:
    grupos = df[col].value_counts()

    fig = go.Figure(
        go.Bar(
            x=grupos.index,
            y=grupos,
            text=grupos,
            textposition="auto",
            marker_color=cores,
        )
    )

    fig.update_layout(
        title=titulo,
        xaxis=dict(tickmode="linear"),
        xaxis_title=xaxis,
        yaxis_title=yaxis,
    )

    return fig


def plot_histograma(
    df: pd.DataFrame, col: str, titulo: str, rug: bool = True
) -> pd.DataFrame:
    # faz o cálculo do KDE com o scipy
    data = df[col].values
    kde = gaussian_kde(data)
    x_vals = np.linspace(min(data), max(data), 1000)
    kde_vals = kde(x_vals)

    # faz o cálculo da quantidade "ótima" de bins (assim evitamos grupos de classificação desnecessários)
    bins = len(np.histogram_bin_edges(data, bins="auto"))

    # cria os plots separados (histograma + kde + rug)
    # 1. histograma
    histogram = go.Histogram(
        x=data, nbinsx=bins, histnorm="probability density", name=f"Densidade: {col}"
    )

    # 2. kde
    kde_line = go.Scatter(
        x=x_vals, y=kde_vals, mode="lines", name="Curva (KDE)", line=dict(color="red")
    )

    # 3. rug, mas apenas se ele tiver sido requisitado
    if rug:
        rug_plot = go.Scatter(
            x=data,
            y=[-0.01] * len(data),
            mode="markers",
            name="Observações individuais",
            marker=dict(color="orange", symbol="line-ns-open", size=10),
        )

    # figura principal
    fig = go.Figure()
    fig.add_trace(histogram)
    fig.add_trace(kde_line)
    fig.update_traces(
        texttemplate="%{y:.2%}", textposition="outside", selector=dict(type="histogram")
    )

    # configs
    fig.update_layout(
        title=titulo,
        xaxis_title="Valor",
        yaxis_title="Frequência",
        yaxis=dict(range=[0, max(kde_vals) + 0.1]),
        bargap=0.015,
        uniformtext_mode="hide",
    )

    # configs com rug
    if rug:
        fig.add_trace(rug_plot)
        fig.update_layout(yaxis=dict(range=[-0.02, max(kde_vals) + 0.1]))
    # configs sem rug
    else:
        fig.update_layout(xaxis=dict(tickmode="linear"))

    return fig


def plot_histograma_comparativo(df: pd.DataFrame, col: str) -> pd.DataFrame:
    fig = px.histogram(
        data_frame=df,
        x=col,
        color="ANO",
        title=f"Distribuição do indicador {col} comparativo",
        nbins=50,
        marginal="rug",
        histnorm="probability density",
    )

    fig.update_traces(
        texttemplate="%{y:.2}", textposition="outside", selector=dict(type="histogram")
    )

    # TODO: não ficou legal... se der tempo, melhorar esse KDE
    # for ano in df['ANO'].unique():
    #     data_year = df[df['ANO'] == ano][col]

    #     kde = gaussian_kde(data_year)
    #     x_vals = np.linspace(min(data_year), max(data_year), 1000)
    #     kde_vals = kde(x_vals)

    #     fig.add_trace(go.Scatter(x=x_vals, y=kde_vals, mode='lines', name=f'KDE {ano}'))

    fig.update_layout(xaxis_title="Valor", yaxis_title="Frequência", height=600)

    return fig


def plot_boxplot(df: pd.DataFrame, col: str, titulo: str) -> pd.DataFrame:
    fig = px.box(y=df[col], points="all", title=titulo)

    fig.update_layout(yaxis_title="Valor")

    fig.update_yaxes(dtick=1)

    return fig


def plot_boxplot_comparativo(df: pd.DataFrame, col: str) -> pd.DataFrame:
    fig = px.box(
        data_frame=df,
        x="ANO",
        y=col,
        points="all",
        title=f"Distribuição do {col} comparativa",
        color="ANO",
    )

    fig.update_layout(yaxis_title="Valor")

    fig.update_yaxes(dtick=1)

    return fig


def plot_boxplot_analise_indicador(
    df_2020: pd.DataFrame,
    df_2021: pd.DataFrame,
    df_2022: pd.DataFrame,
    df_full: pd.DataFrame,
    col: str,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    box_2020 = plot_boxplot(df_2020, col, f"Distribuição do {col} para o ano de 2020")
    box_2021 = plot_boxplot(df_2021, col, f"Distribuição do {col} para o ano de 2021")
    box_2022 = plot_boxplot(df_2022, col, f"Distribuição do {col} para o ano de 2022")
    box_comp = plot_boxplot_comparativo(df_full, col)

    return box_2020, box_2021, box_2022, box_comp

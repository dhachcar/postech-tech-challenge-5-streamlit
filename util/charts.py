from typing import Tuple
import pandas as pd
from scipy.stats import skew, kurtosis, gaussian_kde
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from typing import List

from util.layout import format_number


def classificar_distribuicao_histograma(data):
    kde = gaussian_kde(data)
    diff = np.diff(kde(data))

    modes = data[np.where(diff[:-1] * diff[1:] < 0)[0] + 1]
    skewness = skew(data)
    kurt = kurtosis(data)

    if skewness > 0 and kurt > 3:
        return "Distribuição Assimétrica Positiva e Leptocúrtica"
    elif skewness < 0 and kurt > 3:
        return "Distribuição Assimétrica Negativa e Leptocúrtica"
    elif skewness > 0 and kurt < 3:
        if len(modes) == 2:
            return "Distribuição Bimodal e Platicúrtica"
        elif len(modes) > 2:
            return "Distribuição Multimodal e Platicúrtica"
        else:
            return "Distribuição Assimétrica Positiva e Platicúrtica"
    elif skewness < 0 and kurt < 3:
        if len(modes) == 2:
            return "Distribuição Bimodal e Platicúrtica"
        elif len(modes) > 2:
            return "Distribuição Multimodal e Platicúrtica"
        else:
            return "Distribuição Assimétrica Negativa e Platicúrtica"
    elif skewness == 0 and kurt > 3:
        if len(modes) == 2:
            return "Distribuição Bimodal e Leptocúrtica"
        elif len(modes) > 2:
            return "Distribuição Multimodal e Leptocúrtica"
        else:
            return "Distribuição Simétrica e Leptocúrtica"
    elif skewness == 0 and kurt < 3:
        if len(modes) == 2:
            return "Distribuição Bimodal e Platicúrtica"
        elif len(modes) > 2:
            return "Distribuição Multimodal e Platicúrtica"
        else:
            return "Distribuição Simétrica e Platicúrtica"
    elif skewness > -0.5 and skewness < 0.5 and kurt > 2 and kurt < 3:
        return "Distribuição Mesocúrtica"
    else:
        return "Distribuição com características não convencionais"


def plot_bar(
    df: pd.DataFrame,
    col: str,
    titulo: str,
    xaxis: str,
    yaxis: str = "Quantidade",
    cores: List[str] = None,
):
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
    df: pd.DataFrame,
    col: str,
    titulo: str,
    bins: int = None,
    rug: bool = True,
    analise: bool = False,
):
    # faz o cálculo do KDE com o scipy
    data = df[col].values
    kde = gaussian_kde(data)
    x_vals = np.linspace(min(data), max(data), 1000)
    kde_vals = kde(x_vals)

    # faz o cálculo da quantidade "ótima" de bins (assim evitamos grupos de classificação desnecessários)
    bins = len(np.histogram_bin_edges(data, bins="auto")) if bins == None else bins

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

    # 4. figura principal
    fig = go.Figure()
    fig.add_trace(histogram)
    fig.add_trace(kde_line)
    fig.update_traces(
        texttemplate="%{y:.2%}",
        textposition="outside",
        selector=dict(type="histogram"),
    )

    # 5. faz o cálculo da curtose (achatamento), assimétria, e modos da distribuição
    if analise:
        classificacao = classificar_distribuicao_histograma(data)

        fig.add_annotation(
            x=0,
            y=-0.2,
            xref="paper",
            yref="paper",
            text=f"<b>&nbsp;&nbsp;{classificacao}&nbsp;&nbsp;</b>",
            showarrow=False,
            font=dict(color="black", size=12),
            bgcolor="white",
            borderwidth=1,
            bordercolor="black",
            borderpad=2,
            height=15,
        )

    # 6. configs
    fig.update_layout(
        title=titulo,
        xaxis_title="Valor",
        yaxis_title="Frequência",
        yaxis=dict(range=[-0.02, None]),
        bargap=0.015,
        uniformtext_mode="hide",
    )

    # configs com rug
    if rug:
        fig.add_trace(rug_plot)
    # configs sem rug
    else:
        fig.update_layout(xaxis=dict(tickmode="linear"))

    return fig


def plot_histograma_comparativo(
    df: pd.DataFrame, col: str, barnorm_percent: bool = False
):
    bins = len(np.histogram_bin_edges(df[col], bins="auto"))

    fig = px.histogram(
        data_frame=df,
        x=df[col],
        color="ANO",
        title=f"Distribuição do indicador {col} comparativo e cumulativo",
        nbins=bins,
        marginal="rug",
        histnorm="probability density",
        barnorm=None if not barnorm_percent else "percent",
        cumulative=True,
    )

    fig.update_traces(
        texttemplate="%{y:0.4}",
        textposition="outside",
        selector=dict(type="histogram"),
    )

    # modo específico de output, altera o título
    if barnorm_percent:
        fig.update_traces(
            texttemplate="%{y:0.4}%",
            selector=dict(type="histogram"),
        )
        fig.update_layout(
            title=f"Distribuição do indicador {col} comparativo e cumulativo com as colunas normalizadas",
        )

    fig.update_layout(
        xaxis_title="Valor",
        yaxis_title="Frequência",
        height=600,
        yaxis=dict(range=[-0.02, None]),
        bargap=0.015,
    )

    return fig


def plot_boxplot(df: pd.DataFrame, col: str, titulo: str, calcular_media: bool = False):
    fig = px.box(y=df[col], points="all", title=titulo)

    fig.update_layout(yaxis_title="Valor")

    fig.update_yaxes(dtick=1)

    if calcular_media:
        media = df[col].mean()

        fig.add_shape(
            type="line",
            x0=-0.5,
            x1=0.5,
            y0=media,
            y1=media,
            line=dict(color="red", width=2),
        )

        fig.add_annotation(
            x=0.45,
            y=media,
            text=f"Média: <b>{format_number(media, '%0.2f')}</b>",
            font=dict(color="red", size=14),
            showarrow=False,
            yshift=10,
            align="right",
        )

    return fig


def plot_boxplot_comparativo(df: pd.DataFrame, col: str):
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

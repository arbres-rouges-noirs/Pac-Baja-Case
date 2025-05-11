import pandas as pd
import plotly.express as px

def data_ploting(weeks: list, index: list) -> pd.DataFrame:
    df = pd.DataFrame([weeks])
    df.columns = index
    return df

def plot_graphs(df: pd.DataFrame, x: str, y: str) -> px.histogram:
    fig = px.histogram(df, x, y, histfunc='avg')

    return fig
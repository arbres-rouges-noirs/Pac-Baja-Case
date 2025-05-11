import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def create_heatmap(df: pd.DataFrame, rc: dict) -> sns.heatmap:
    # Sample dat
    labels = ['kpi_01', 'kpi_02', 'kpi_03','kpi_04']

    #key_index_1 = [19, 25, 35]
    #key_index_2 = [20, 15, 12]
    #key_index_3 = [90.14, 75, 82]
    key_index_4 = [60, 73, 57]

    #key_indexes_matrix = np.array([key_index_1,key_index_2,key_index_3,key_index_4]).transpose()
    #df = pd.DataFrame(key_indexes_matrix, columns=labels)

    corr = df.corr(numeric_only=True)
    sns.set_theme(rc=rc)
    fig, ax = plt.subplots()
    heatmap = sns.heatmap(
        corr,
        annot=True,
        cmap='viridis',
        ax=ax,
        annot_kws={"color": "white"})

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    colorbar = heatmap.collections[0].colorbar

    # Change tick label color
    colorbar.ax.yaxis.set_tick_params(color='white')
    colorbar.ax.yaxis.set_ticklabels(colorbar.ax.get_yticklabels(), color='white')

    st.subheader("Correlação entre KPIs")
    st.pyplot(fig)
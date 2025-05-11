import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from annotated_text import annotated_text

def main() -> None:
    st.set_page_config(layout="wide")
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #141414;
            color: #ffde21;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("📊 Monitoramento de KPIs - Projeto PAC Baja ")
    st.write("Paleta de Cores usada no Dashboard e nos gráficos inspirada no Salamandra 🦎:car:")
    
    weeks = ["Semana 1","Semana 2","Semana 3"]
    key_index_1 = [19, 25, 35]
    key_index_2 = [20, 15, 12]
    key_index_3 = [90.14, 75, 82]
    key_index_4 = [60, 73, 57]
    labels_kpi = ['KPI 01', 'KPI 02', 'KPI 03','KPI 04']

    key_indexes_matrix = np.array([key_index_1,key_index_2,key_index_3,key_index_4])

    data = { 
            'Semanas': weeks,
            'Indices': ['Indice_01','Indice_02','Indice_03'],
            'Indice_01': key_index_1,
            'Indice_02': key_index_2,
            'Indice_03': key_index_3,
            'Indice_04': key_index_4
            }

    chart_data = pd.DataFrame(key_indexes_matrix,columns=["1","2","3"])

    df = pd.DataFrame(data)
    col1, col2, col3, col4 = st.columns(4)
    sns.set_theme(rc={'axes.facecolor':'#141414', 'figure.facecolor':'#141414'})
    with col1:
        st.subheader("KPI 1: Quantidade de Erros no Carro")
        fig1, ax1 = plt.subplots()
        sns.barplot(df, x='Semanas', y='Indice_01',ax=ax1, color="#FFDE21", legend=False)

        ax1.tick_params(axis='x', colors='white')
        ax1.tick_params(axis='y',colors='white')
        ax1.set_ylabel('')
        ax1.set_xlabel('')
        st.pyplot(fig1)

        st.subheader('Correlação entre KPIs')
        fig5, ax5 = plt.subplots()

        rc = {'axes.facecolor':'#141414', 'figure.facecolor':'#141414'}
        df2 = pd.DataFrame(key_indexes_matrix.transpose(),columns=labels_kpi)
        corr = df2.corr(numeric_only=True)
        sns.set_theme(rc=rc)
        heatmap = sns.heatmap(
            corr,
            annot=True,
            cmap='viridis', 
            ax=ax5,
            annot_kws={"color": "white"})
        ax5.tick_params(axis='x',colors='white')
        ax5.tick_params(axis='y',colors='white')
        colorbar = heatmap.collections[0].colorbar


        colorbar.ax.yaxis.set_tick_params(color='white')
        colorbar.ax.yaxis.set_ticklabels(colorbar.ax.get_yticklabels(), color='white')
        st.pyplot(fig5)

        st.caption('Valor mais próximo de 1: relação linear diretamente proporcional')
        st.caption('Valor igual a 0: não há relação linear')
        st.caption('Valor mais próximo de -1: relação linear inversamente proporcional')
    


    
    with col2:
        st.subheader("KPI 2: Faltas não justificadas < 16.67%")
        fig2, ax2 = plt.subplots()
        sns.barplot(df, x='Semanas', y='Indice_02',ax=ax2, color="#FFDE21")

        ax2.tick_params(axis='x', colors='white')
        ax2.tick_params(axis='y',colors='white')
        ax2.set_ylabel('')
        ax2.set_xlabel('')
        st.pyplot(fig2)

        st.subheader("Média Equipe com Atividades entregues a tempo*")
        st.write("*Em três semanas")
        fig,ax = plt.subplots()
        mean_value = np.mean(key_index_3)
        list = [mean_value, 100 - mean_value]
        labels_pie_1 = ['% com tarefas entregues a tempo', '% com tarefas não entregues a tempo']
        color_palette = sns.color_palette("viridis")
        wedges, texts, autotexts = ax.pie(list, labels=labels_pie_1,colors=color_palette, autopct='%.0f%%')
        for text in texts:
            text.set_color('white') 
        for autotext in autotexts:
            autotext.set_color('white')
        ax.axis('equal')

        st.pyplot(fig)
    
    with col3:
        st.subheader("KPI 3: Tarefas entregues a tempo")
        fig3, ax3 = plt.subplots()
        sns.barplot(df, x='Semanas', y='Indice_03',ax=ax3, color="#FFDE21")

        ax3.tick_params(axis='x', colors='white')
        ax3.tick_params(axis='y',colors='white')
        ax3.set_ylabel('')
        ax3.set_xlabel('')
        st.pyplot(fig3)

        st.subheader("Média Interações Facultativas*")
        st.write("*Em três semanas")
        fig,ax = plt.subplots()
        color_palette = sns.color_palette("viridis")
        mean_value = np.mean(key_index_4)
        list = [mean_value, 100 - mean_value]
        labels_pie_2=['% da Equipe com 70% de interações facultativas', '% da Equipe com interações facultativas < 70%']
        wedges, texts, autotexts = ax.pie(list, labels=labels_pie_2,colors=color_palette, autopct='%.0f%%')
        for text in texts:
            text.set_color('white') 
        for autotext in autotexts:
            autotext.set_color('white')


        st.pyplot(fig)

        #df = data_ploting(weeks=weeks, index=key_index_1)
        #print(df)

    with col4:
        st.subheader('KPI 4: Porcentagem Interações Facultativas')
        fig4, ax4 = plt.subplots()
        sns.barplot(df, x='Semanas', y='Indice_04',ax=ax4, color="#FFDE21")

        ax4.tick_params(axis='x', colors='white')
        ax4.tick_params(axis='y',colors='white')
        ax4.set_ylabel('')
        ax4.set_xlabel('')
        st.pyplot(fig4)

        #fig4 = px.bar(df, x='Semanas', y='Indice_04')
        #fig4.update_traces(marker_color="#FFDE21", marker_pattern_bgcolor="#141414")
        #col4.plotly_chart(fig4, use_container_width=True)


if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload file",type=["csv"])

if file is not None:
    df = load_data(file)

    n_rows = st.slider("Choose number of rows",5,max_value=len(df),step=1)

    

    n_columns = st.multiselect("Select columns to show",df.columns.to_list(),default=df.columns.to_list())

    numerical_columns = df.select_dtypes(include=np.number).columns.to_list()

    st.write(df[:n_rows][n_columns])

    tab1 , tab2 = st.tabs(["Scatter plot","Histogram"])
    with tab1:


        col1 , col2 , col3 = st.columns(3)

        with col1:
            X_select = st.selectbox("Select column on x axis",numerical_columns)

        with col2:
            Y_select = st.selectbox("Select column on y axis",numerical_columns)

        with col3:
            color = st.selectbox("Select color",df.columns)
        figure_scatter = px.scatter(df,x = X_select , y = Y_select,color=color)
        
        st.plotly_chart(figure_scatter)
    
    with tab2:

        histogram_feature = st.selectbox("Select feature to histogram",numerical_columns)


        figure_hist = px.histogram(df , x = histogram_feature)
        st.plotly_chart(figure_hist)

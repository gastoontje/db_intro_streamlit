import pandas as pd
import sqlite3
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide", page_title="Belgium Enterprises Visualization", page_icon = 'App_Icon.png')

load_page = False


# Check if a dataframe has been created from upload in Homepage
if 'df' in st.session_state :
    df = st.session_state['df']
    load_page = True
else:
    st.write('Upload a file on Homepage first')


# If yes then we can work on it
if load_page:
       st.text('We can see that 100% of the enterprises in the database have the AC (=Active) status')


       df = df.groupby(['Status'])['Status'].count().reset_index(name="Count")


       col1, col2 = st.columns(2)

       x_axis_val = col1.selectbox('Select the X-axis', options=df.columns, index=0)
       y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns, index=1)

       plot = px.histogram(df, x=x_axis_val, y=y_axis_val).update_xaxes(categoryorder='total descending')
       st.plotly_chart(plot, use_container_width=True)

       df

hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

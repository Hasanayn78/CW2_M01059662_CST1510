import streamlit as st
import pandas as pd
from APP.icidents import get_all_cyber_incidents     
from APP.db import get_connection              


conn = get_connection()


df = get_all_cyber_incidents(conn)



st.set_page_config(layout='wide')
st.title('cyber_inncident Dashboard')


with st.sidebar:
    severities  = st.selectbox('Severity', df['severity'].unique())

df['timestamp'] = pd.to_datetime(df['timestamp'])
filter  = df[df['severity']== severities]

col1, col2 = st.columns(2)

with col1:
    st.subheader('cyber_inncident by Name')
    st.bar_chart(filter, x='category', y='incident_id')

with col2:
    st.subheader('cyber_inncident by Category')
    st.line_chart(filter, x='timestamp', y='incident_id')


# Show the table
st.dataframe(filter)

# Extra text
st.title('Welcome to cyber_inncident Page')
st.write('hello world')
st.header('cyber_inncident Header')
st.subheader('subheader')

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/youridibbet.jpg", width=300)

with col2:
    st.title('Youri Dibbet')
    content = '''
    Hi, I am Youri!  \n
    This website is to show everyone what I have made thus far using Python!
    '''
    st.info(content)

content2 = '''
Below you will find some of the apps I made using Python.Feel free to contact me about any of them!
'''
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source Code]({row['url']})")
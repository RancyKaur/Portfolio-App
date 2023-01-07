import streamlit as st

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Rancy Chadha")
    content='''
    Hey There! I am Rancy! I am a coding enthusiast and evergreen learner! 
    Professionally I am a SharePoint Engineer but my passion to be a Data Scientist and a web developer 
    has motivated me to learn Python and utilize it for my personal projects. 
    I am also currently a graduate student studying MApCompScience from Concordia University, Montreal
    '''
    st.info(content) # this introduce light blue background to the text
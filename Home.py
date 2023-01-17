import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.title("Rancy Chadha")
col1,col2 = st.columns(2)
with col1:
    st.image("images/photo.png")#,width=550)

with col2:
    #st.title("Rancy Chadha")
    content='''
    Hey There! I am Rancy. I have worked extensively on Microsoft M365 solutions and I specialize on SharePoint.
    I have worked with various organizations like Microsoft, L&T Infotech, Accenture.
    I am very passionate about coding and I strongly believe in keeping oneself updated and to keep learning. 
    Web development has always enticed me along with that I like to do data mining to drive insights from data. 
    Data and the magic that can be done with it, has motivated me to learn various forms of ML techniques. 
    Oh and one last fact about me :) 
    I am currently a graduate student and pursuing MApCompScience starting Fall 2022 from Concordia University, Montreal
    '''
    st.info(content) # this introduce light blue background to the text

content2 ='''
          The list below showcases few projects that I am currently working on. Feel free to reach out to me to find out more!
          '''
st.write(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
projects_df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in projects_df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in projects_df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

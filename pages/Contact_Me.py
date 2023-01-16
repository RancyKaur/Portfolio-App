import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="messageformid"):
    UserEmail = st.text_input("Your Email Address")
    rawMsg = st.text_area("Your Message:")
    button = st.form_submit_button("Submit")
    UserMsg = f'''\
Subject: New email from {UserEmail}

From: {UserEmail}
{rawMsg}
'''
    if button:
        send_email(UserMsg)
        st.info("Your message is sent!")
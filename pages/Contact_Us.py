import streamlit as st
from sendmail import send_email

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input('Enter your email adress')
    raw_message = st.text_area("Your message here")
    message = f'''\
Subject: New email from {user_email}
{raw_message}
'''
    user_send = st.form_submit_button()
    if user_send:
        send_email(message)
        st.info('Your email was send successfully')
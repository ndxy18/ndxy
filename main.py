import streamlit as st
import pandas as pd
name = st.text_input("Enter your name:" )
fname = st.text_input("Enter your father name: ")
adress = st.text_area("Enter your adress: ")
classdata = st.selectbox("select your class :",(1,2,3,4,5,6,))

button = st.button("Click me")
if button:
    st.markdown(f"""
    Name : {name}
    father : {fname}
    address : {adress}
    classdata : {classdata}""")














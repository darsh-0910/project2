import streamlit as st
st.title("hello Streamlit")
name = st.text_input("enter your name:")
if st.button("Submit"):
    st.success(f"Welcome {name}")
import streamlit as st

st.title("AI PDF Chatbot")

uploaded_file = st.file_uploader("Upload your PDF")

question = st.text_input("Ask a question")

if uploaded_file and question:
    st.write("AI response will appear here.")

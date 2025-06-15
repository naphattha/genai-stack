import streamlit as st
from chains.finance import run_finance_chatbot

st.set_page_config(page_title="SET50 Financial Chatbot")
st.title("📊 Financial Knowledge Graph Chatbot")

question = st.text_input("Ask a financial question about SET50:")
if st.button("Submit"):
    with st.spinner("Thinking..."):
        answer = run_finance_chatbot(question)
        st.markdown(answer)

import streamlit as st
from utils import write_message
from agent_mysql import generate_response as generate_sql_response
from agent_neo4j import generate_response as generate_neo4j_response
from langchain.globals import set_debug
from external_api import call_openai
# เปิดโหมด debug ให้ LangChain แสดง reasoning ทุกขั้น
set_debug(True)

st.set_page_config("Finance bot", page_icon=":coin:")

# session state messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your financial assistant. How can I help you today?"},
    ]

if "query_logs" not in st.session_state:
    st.session_state.query_logs = []

# แสดงข้อความก่อนหน้า
for message in st.session_state.messages:
    write_message(message['role'], message['content'], save=False)

# UI: Select database for this query
db_option = st.selectbox("Select the database for this question", ["mysql", "neo4j"], key="db_select")

# Get user input
prompt = st.chat_input("Ask your question...")

# prompt = "ช่วยสรุปงบกำไรขาดทุนบริษัท AOT ให้หน่อย"
# response, error = call_openai(prompt)

if prompt:
    # แสดงข้อความผู้ใช้
    write_message('user', prompt)

    # เรียก generate_response ตามฐานข้อมูลที่เลือก
    if db_option == "mysql":
        response, metadata, error = generate_sql_response(prompt)
    else:  # neo4j
        response, metadata, error = generate_neo4j_response(prompt)

    if error:
        st.error(f"❌ error: {error}")
    elif response:
        write_message('assistant', response)

    # เก็บข้อความใน session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    if response:
        st.session_state.messages.append({"role": "assistant", "content": response})

import streamlit as st
from ai import gemini_ai
from prompt import WELCOME_MESSAGE

st.header("Welcome to Quote Generator", anchor="False")

#Create messages
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "user", "content": WELCOME_MESSAGE}]

# get chat from client
chat = gemini_ai()

#load Chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Respond with topic!"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        reply = chat.send_message(prompt)
        response = st.markdown(reply.text)
        st.session_state.messages.append({"role": "assistant", "content": reply.text})





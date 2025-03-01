import streamlit as st
import requests

API_URL = "http://backend:8000/generate"  
st.title("Gemini LLM Chatbot")
st.write("Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    try:
        response = requests.post(API_URL, json={"query": user_input})
        bot_response = response.json().get("response", "Error: No response.")

        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.chat_message("assistant").write(bot_response)

    except Exception as e:
        st.error(f"Error: {e}")

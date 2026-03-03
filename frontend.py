import streamlit as st
import requests

st.title("Welcome to your AI therapist")
st.write("Are you feeling OK? Feel free I can help you")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

if st.button("Send") and user_input:
    response = requests.post("http://localhost:5000/chat", json={"message": user_input})
    st.session_state.chat_history.append(("You", user_input))
    bot_reply = response.json()["reply"]
    st.session_state.chat_history.append(("Bot", bot_reply))

for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")

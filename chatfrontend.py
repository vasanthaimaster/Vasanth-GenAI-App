import streamlit as st
import chatbackend as glib

st.set_page_config(page_title="GenAI App", page_icon=":robot:")
st.title('GenAI App')

# Initialize memory
if 'memory' not in st.session_state:
    st.session_state.memory = glib.create_memory()

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Re-render chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# Input box
input_text = st.chat_input("Chat with the bot")

if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Get chatbot response
    chat_response = glib.get_chat_response(input_text=input_text, memory=st.session_state.memory)

    with st.chat_message("AI"):
        st.markdown(chat_response)
    st.session_state.chat_history.append({"role": "AI", "text": chat_response})

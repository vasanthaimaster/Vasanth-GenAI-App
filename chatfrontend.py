# import streamlit and chatbackend python file

import streamlit as st # all streamlit commands will be avaiable throught the "st" alias
import chatbackend as glib # referencet to loald lib script
from chatbackend import titan_llm

# here we are setting the page title on the actual page and the title shown in the browser tab
st.set_page_config(page_title="GenAI App", page_icon=":robot:") # HTML Title
st.title('GenAI App') # Page Title


# Initialize the Memory
if 'memory' not in st.session_state: # see if the memory hasn't been created yet
    st.session_state.memory = glib.create_memory() # initialize the memory

# Intialize the Chat History
if 'chat_history' not in st.session_state: # see if the chat history hasn't been created yet
    st.session_state.chat_history = [] # initialize the chat history

# Re-render the chat history(Stremalit re-runs this script, so need this to preserve chat messages)
for message in st.session_state.chat_history: # loop through the chat history
    with st.chat_message(message["role"]): # renders a chat line for the history messages
        st.markdown(message["text"]) # display the chat content

# create a chat input box
input_text = st.chat_input("Chat with the bot") # WIDGET: input field for text. 

# code for displaying User's and Bot's chat messages
if input_text: # if there is input text
    with st.chat_message("user"): # display the user's chat message
        st.markdown(input_text) # renders the user's chat message
    st.session_state.chat_history.append({"role":"user", "text":input_text}) # append the user's message to the chat history
    chat_response = glib.get_chat_response(input_text=input_text, memory=st.session_state.memory) # call the chatbot function
    with st.chat_message("AI"): # display the bot's chat message
        st.markdown(chat_response) # renders the bot's chat message
    st.session_state.chat_history.append({"role":"AI", "text":chat_response}) # append the bot's message to the chat history
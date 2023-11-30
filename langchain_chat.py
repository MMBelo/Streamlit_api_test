import os
import streamlit as st
from langchain import LangChain
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = st.secrets["key1"]
client = OpenAI()


# Create LangChain with OpenAI as the language model
lang_chain = LLMChain()

# Create a conversation memory
conversation_memory = ConversationBufferMemory(input_key='user_input', memory_key='chat_history')

# Streamlit app
st.title('LangChain Chatbot with Memory')

# User input
user_input = st.text_input('You:')

# Generate response when the user clicks a button
if st.button('Get Response'):
    # Add user input to conversation history
    conversation_history = conversation_memory.read()
    conversation_history.append(user_input)
    conversation_memory.write(conversation_history)

    # Generate response using LangChain
    response = lang_chain.run(user_input, memory={'chat_history': conversation_history})

    # Add AI response to conversation history
    conversation_history.append(response)
    conversation_memory.write(conversation_history)

    # Display AI response
    st.text_area('Chatbot:', response, height=100)

# Display conversation history
st.text_area("Conversation History", "\n".join(conversation_memory.read()), height=200)

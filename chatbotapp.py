# Bring in deps
import os

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
#from langchain.schema.messages import HumanMessage, SystemMessage
#from langchain import LangChain


os.environ['OPENAI_API_KEY'] = st.secrets["key"]

# App framework
st.title('🤖🍞 Talking toaster AI')
prompt = st.text_input('Ask the Toaster')

title_template = PromptTemplate(input_variables = ['topic'], template="Your name is Talking Toaster, As an experienced Electric Engineer specializing in household appliances or electronic equipment, your task is to assist individuals with no technical background in identifying and addressing technical issues. Maintain a helpful, friendly, clear, and concise tone throughout. Start by briefly describing the product and confirming its equipment and model. Then, identify the issue and seek clarification with up to two simple, non-technical questions if needed. Provide a straightforward solution. Highlight common mis practices for the equipment. If the repair is too technical or potentially hazardous, advise seeking support from the equipments brand or hiring a specialized technician. answer: {topic}")

# Memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

# Llms
llm = OpenAI(temperature=0.9)

title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)#, output_key='title', memory=title_memory)

# Show stuff to the screen if there's a prompt
if prompt:
    response = title_chain.run(topic=prompt)

st.write("IAM RESPONSE "+ response)  ## comented

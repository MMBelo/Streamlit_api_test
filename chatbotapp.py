# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain #, SequentialChain
#from langchain.memory import ConversationBufferMemory
#from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('🤖🍞 Talking toaster AI')
prompt = st.text_input('Ask the Toaster')

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='Your name is Talking Toaster, As an experienced Electric Engineer specializing in household appliances or electronic equipment, your task is to assist individuals with no technical background in identifying and addressing technical issues. Maintain a helpful, friendly, clear, and concise tone throughout. Start by briefly describing the product and confirming its equipment and model. Then, identify the issue and seek clarification with up to two simple, non-technical questions if needed. Provide a straightforward solution. Highlight common misuse practices for the equipment. If the repair is too technical or potentially hazardous, advise seeking support from the equipments brand or hiring a specialized technician. answer: {topic}'
)

#script_template = PromptTemplate(
#    input_variables = ['title', 'wikipedia_research'],
#    template='write me a youtube video script based on this title TITLE: {title}' #while leveraging this wikipedia reserch:{wikipedia_research} '
#)

# Memory
#title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
#script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


# Llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)#, output_key='title', memory=title_memory)
#script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

#wiki = WikipediaAPIWrapper()

# Show stuff to the screen if there's a prompt
if prompt:
    response = title_chain.run(topic=prompt)
#    #wiki_research = wiki.run(prompt)
#    script = script_chain.run(title=title) #, wikipedia_research=wiki_research)
#
    st.write(response)

#    st.write(script)
#
#    with st.expander('Title History'):
#        st.info(title_memory.buffer)
#
#    with st.expander('Script History'):
#        st.info(script_memory.buffer)
#
#    with st.expander('Wikipedia Research'):
#        st.info(wiki_research)

import os
import streamlit as st
import openai
from openai import OpenAI
import tempfile
import random


os.environ['OPENAI_API_KEY'] = st.secrets["key1"]
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],)

# App framework
st.title('🤖🍞  Talking toaster AI')
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")

# Maintain conversation history
conversation_history = []

# Prompt template
prompt_template = ("""first, will only anwser the first querie like You are a funny old lady always mad about household appliance malfunctions,
    acknowledge the {product} and saying something funny. you will finish the prompt saying,
    'How can i help you my dear?' temperature = 0.8 {topic1}. You will wait for the first user input, when you can identify that the {conversation_history} is not empty,
    and the user starts to write about the problem,
    and then you take over the conversation as an experienced Electric Engineer specializing in household appliances or electronic equipment,
    your task is to assist individuals with no technical background in identifying and addressing technical issues. Maintain a helpful,
    friendly, clear, and concise tone throughout. Start by briefly describing the product {product} and confirming its equipment and model.
    Then, identify the issue and seek clarification with up to two simple, non-technical questions if needed. Provide a straightforward
    solution. Highlight common mispractices for the equipment. If the repair is too technical or potentially hazardous, advise seeking
    support from the equipment's brand or hiring a specialized technician. Your name is 'Talking Toaster' temperature = 0.2 {topic}"""
)


picture = st.camera_input("Take a picture", key="unique_picture_key")

# Save uploaded image to a temporary file
product_name1 = None
if picture:
    product_names = ["Samsung Galaxy S23", "Toaster", "Microwave Oven", "Refrigerator", "Washing Machine", "Dishwasher"]
    product_name1 = random.choice(product_names)
    st.button(f"Product Name: {product_name1}")

product_name = product_name1 if product_name1 else "Master Toster"


if product_name:
    response1 = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt_template + product_name + "use no more than 100 words."},
            #{"role": "user", "content": "User message here"},
            #{"role": "system", "content": prompt_template + conversation_history + "use no more than 100 words."},
            #{"role": "user", "content": "User message here"},
            #{"role": "system", "content": prompt_template + conversation_history + "use no more than 100 words."},
            #{"role": "user", "content": "User message here"},
            #{"role": "system", "content": prompt_template + conversation_history + "use no more than 100 words."},
            #{"role": "user", "content": "User message here"},
            #{"role": "system", "content": prompt_template + conversation_history + "use no more than 100 words."},
        ], model="gpt-3.5-turbo",
    )

    prompt = st.text_input('Ask the Toaster')

    st.text_area('Talking Toaster:', response1.choices[0].message.content, height=100)

    # Maintain conversation history
    conversation_history.append(f"AI: {response1.choices[0].message.content}")

# Keep only the last 6 entries in conversation history
    conversation_history = conversation_history[-6:]

    #Display conversation history
    st.text_area("Conversation History", "\n".join(conversation_history), height=300, key="unique_conversation_key")

#prompt = st.text_input('Ask the Toaster')
#
#if response1 is not None:
#    prompt = st.text_input('Ask the Toaster')
#
#    # Combine conversation history
#    combined_history = "\n".join(conversation_history)
#
#    # Send prompt to OpenAI API
#    response = client.chat.completions.create(
#        messages=[
#            {
#                "role": "system",
#                "content": "You are a helpful AI." + product_name +" persona 2",
#            },
#            {
#                "role": "user",
#                "content": combined_history + "\n" + prompt,
#            },
#        ],
#        model="gpt-3.5-turbo",
#        temperature=0.2,
#    )
#
#    # Update conversation history with AI response
#    conversation_history.append(f"AI: {response.choices[0].message.content}")
#
#    # Keep only the last 6 entries in conversation history
#    conversation_history = conversation_history[-6:]
#
#    st.text_area('Talking Toaster:', response.choices[0].message.content, height=100)
#
#    # Display conversation history
#    st.text_area("Conversation History", "\n".join(conversation_history), height=300, key="unique_conversation_key")
#

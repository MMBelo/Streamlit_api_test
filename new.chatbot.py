import os
import streamlit as st
import openai
from openai import OpenAI
import tempfile

os.environ['OPENAI_API_KEY'] = st.secrets["key1"]
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],)

# App framework
st.title('🤖🍞  Talking toaster AI')
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")

picture = st.camera_input("Take a picture")

# Function to save uploaded image to a temporary file
def save_uploaded_image(picture):
    if picture is not None:
        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
            temp_file.write(picture.read())
            temp_file.flush()
            return temp_file.name
    else:
        return None

# Maintain conversation history
conversation_history = []

# Prompt template
prompt_template = (
    "Your name is Talking Toaster. As an experienced Electric Engineer specializing in household appliances or electronic equipment, "
    "your task is to assist individuals with no technical background in identifying and addressing technical issues. Maintain a helpful, "
    "friendly, clear, and concise tone throughout. Start by briefly describing the product and confirming its equipment and model. "
    "Then, identify the issue and seek clarification with up to two simple, non-technical questions if needed. Provide a straightforward "
    "solution. Highlight common mispractices for the equipment. If the repair is too technical or potentially hazardous, advise seeking "
    "support from the equipment's brand or hiring a specialized technician. Answer: {topic}"
)
prompt_object_detected = """You are a funny old lady always mad about household appliance malfunctions,
                            acknowledge the product name '(samsung1000)' say something funny. Finish the prompt saying,\
                            'How can i help you my dear?Answer: {topic1}'"""

# Function to generate first interaction with object detected and user using OpenAI API
def generate_object_response(picture, prompt_object_detected):
    if picture:
        st.image(picture)

        try:
            # Generate response for pbject detection
            response1 = client.chat.completions.create(
            messages=[
                    {"role": "system", "content": "You are a funny old lady that will talk about the 'object name'"},
                    {"role": "user", "content": "\n" + prompt_object_detected.format(topic1=prompt)}
                ], model="gpt-3.5-turbo", temperature=0.8,
            )
             # Add AI response to the conversation history
            conversation_history.append(f"AI: {response1.choices[0].message.content}")
            # Keep only the last 6 entries in the conversation history
            conversation_history = conversation_history[-6:]
            return response1.choices[0].message.content
            #response = generate_object_response(prompt, conversation_history, temperature=0.8, prompt_object_detectede=prompt_object_detected)

        except Exception as e:
            st.error(f"Error generating response: {e}")
            return None


# Function to generate first response box
def generate_first_user_text_input(response1):
    if response1:
        st.text_area('Talking Toaster:', response1, height=300)
    else:
        st.error(f"Error generating response:")
        return None

# Main conversation loop
while True:
    prompt = st.text_input('Ask the Toaster')
    st.button('Get Response')


# Function to generate first response box
    def generate_first_user_text_input(prompt, prompt_template, response, conversation_history, combined_history):

        if st.button() and prompt:
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "Your name is Talking Toaster. your task is to assist individuals with no technical background in identifying and addressing technical issues."},
                    {"role": "user", "content": combined_history + "\n" + prompt_template.format(topic=prompt)}
                ], model="gpt-3.5-turbo", temperature=0.2,
            )
             # Add AI response to the conversation history
            conversation_history.append(f"AI: {response.choices[0].message.content}")
            # Keep only the last 6 entries in the conversation history
            conversation_history = conversation_history[-6:]
        if response:
            st.text_area('Talking Toaster:', response, height=300)

# Display conversation history
        st.text_area("Conversation History", "\n".join(conversation_history), height=300)

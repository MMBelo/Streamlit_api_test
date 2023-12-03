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
prompt_template = (
    "Your name is Talking Toaster. As an experienced Electric Engineer specializing in household appliances or electronic equipment, "
    "your task is to assist individuals with no technical background in identifying and addressing technical issues. Maintain a helpful, "
    "friendly, clear, and concise tone throughout. Start by briefly describing the product {} and confirming its equipment and model. "
    "Then, identify the issue and seek clarification with up to two simple, non-technical questions if needed. Provide a straightforward "
    "solution. Highlight common mispractices for the equipment. If the repair is too technical or potentially hazardous, advise seeking "
    "support from the equipment's brand or hiring a specialized technician. Answer: {topic}"
)
prompt_object_detected = ("""You are a funny old lady always mad about household appliance malfunctions,
                            acknowledge the {} say something funny. Finish the prompt saying,
                            'How can i help you my dear?{topic1}'""")


picture = st.camera_input("Take a picture", key="unique_picture_key")

#
#if st.button("Generate Product Name..."):
#    product_names = ["Samsung Galaxy S23", "Toaster", "Microwave Oven", "Refrigerator", "Washing Machine", "Dishwasher"]
#    product_name = random.choice(product_names)
#    if product_name:
#        selected_product = product_name
#        st.success(f"Product Name: {product_name}")
#
#        # Use the variable in other functions
#        print(f"Selected product: {selected_product}")



# Save uploaded image to a temporary file
if picture:
    product_names = ["Samsung Galaxy S23", "Toaster", "Microwave Oven", "Refrigerator", "Washing Machine", "Dishwasher"]
    product_name1 = random.choice(product_names)
    if st.button(f"Product Name: {product_name1}"):
#    try:
#        with tempfile.NamedTemporaryFile(delete=True) as temp_file:
#            temp_file.write(picture.read())
#            temp_file.flush()
#            temp_file.close()
#    except Exception as e:
#        st.error(f"Error saving image: {e}")


# Function to generate first interaction with object detected and user using OpenAI API
#def generate_object_response(product_name, prompt_object_detected,conversation_history):
#if product_name1:
#    if st.button('Start Chat:'):
        # Add current user prompt to the conversation history
        #conversation_history.append(f"Product: {product_name1}")
        response1 = client.chat.completions.create(
            messages=[
                    {"role": "system", "content": "You are a funny old lady that will talk about the" + product_name1 +""},
                    {"role": "user", "content": "\n" + prompt_object_detected.format(topic1=prompt_object_detected)}
                ], model="gpt-3.5-turbo", temperature=0.8,
            )
            # Add AI response to the conversation history
    conversation_history.append(f"AI: {response1.choices[0].message.content}")
            # Keep only the last 6 entries in the conversation history
    conversation_history = conversation_history[-6:]
    if response1:
         first_interaction = st.text_area('Talking Toaster:', response1, height=300)
else:
        st.error(f"Error generating response:")


prompt = None
while True:
  if first_interaction:
       # Prompt input is not available, display it
        prompt = st.text_input("Ask the Toaster", key="unique_prompt_key")

        if st.button("Get Response", key="unique_button_key"):
            combined_history = "\n".join(conversation_history)
            response = client.chat.completions.create(
            messages=[
          {"role": "system", "content": "Your name is Talking Toaster. Your task is to assist individuals with no technical background in identifying and addressing technical issues."},
          {"role": "user", "content": combined_history + "\n" + prompt_template.format(topic=prompt)}
        ],
        model="gpt-3.5-turbo", temperature=0.2
      )

      # Add AI response to the conversation history
        conversation_history.append(f"AI: {response.choices[0].message.content}")

      # Keep only the last 6 entries in the conversation history
        conversation_history = conversation_history[-6:]

        if response:
            st.text_area("Talking Toaster:", response, height=300, key="unique_response_key")



    # Display conversation history
        st.text_area("Conversation History", "\n".join(conversation_history), height=300, key="unique_conversation_key")

import os
import streamlit as st
import openai
# Set your OpenAI API key
os.environ['OPENAI_API_KEY'] = "your-api-key"
# App framework
st.title('🤖🍞  Talking toaster AI')
prompt = st.text_input('Ask the Toaster')
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
# Function to generate response using OpenAI API
def generate_response(prompt, conversation_history):
    if prompt:
        # Add current user prompt to the conversation history
        conversation_history.append(f"User: {prompt}")
        try:
            # Combine the conversation history with the prompt template
            combined_history = "\n".join(conversation_history)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Updated model name
                messages=[
                    {"role": "system", "content": "You are a helpful AI."},
                    {"role": "user", "content": combined_history + "\n" + prompt_template.format(topic=prompt)}
                ]
            )
            # Add AI response to the conversation history
            conversation_history.append(f"AI: {response['choices'][0]['message']['content']}")
            # Keep only the last 6 entries in the conversation history
            conversation_history = conversation_history[-6:]
            return response['choices'][0]['message']['content']
        except Exception as e:
            st.error(f"Error generating response: {e}")
            return None
# Display response
if st.button('Get Response'):
    response = generate_response(prompt, conversation_history)
    if response:
        st.text_area('Talking Toaster:', response, height=300)
# Display conversation history
st.text_area("Conversation History", "\n".join(conversation_history), height=300)

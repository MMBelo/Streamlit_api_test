import streamlit as st
from functions import *
from main import*
from Louismodel_id import *
from Arnaud_chaindocs import*


def run():
    # App framework
    st.title('🤖🍞 Talking toaster AI')
    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        fridge = execute_1(uploaded_image)

        a = lemmatizing_manual()

        if fridge:

            manual = file_selection(fridge)

            st.write("I see that you have a "+ fridge + "please let me know how can i assist you?")

            user_input = st.text_input('')

            if user_input:

                answer = retrieve_answer(user_input)

                st.write(answer)



#stremlit file uploader
#
#def main():
#    st.title("Image Uploader")
#
#    # Upload image through Streamlit
#    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
#
#    # Display the uploaded image
#    if uploaded_image is not None:
#        st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)
#
#        # Process the image or store it in a variable
#        # For example, you can convert the image to bytes and store it in a variable
#        image_bytes = uploaded_image.read()
#
#        # Now 'image_bytes' contains the binary data of the uploaded image
#        return image_bytes

## get the object, type, brand, and model and start the conversation

## if upload is true





if __name__ == '__main__':
    run()



## Recive model result # if fridge = Samsung 1000
## Samsung 1000 should be the first input/conversation starter in chatbot


##Chatbot recives the first input and answers with the prompt and knowledge from the manual of the fridge



#from chatbotapp import give_response

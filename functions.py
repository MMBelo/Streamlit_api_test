from chatbotapp import give_response

def execute_1(uploaded_image):
    image = uploaded_image
    if image:
        fridge = 'Samsung1000'
        return fridge

def send_product_name():
    product = execute_1()
    return product



def retrieve_answer(prompt):
    if prompt:
        manual = give_response(prompt)
        return manual

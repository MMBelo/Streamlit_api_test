from chatbotapp import give_response
from predict import predict

def execute_1(uploaded_image):
    image = uploaded_image
    if image:
        fridge = predict(image)
        return fridge

def send_product_name():
    product = execute_1()
    return product



def retrieve_answer(prompt):
    if prompt:
        manual = give_response(prompt)
        return manual


def vect_pdf(manual_pdf):

    return manual_pdf_vectorized

def lem_vect_pdf(vect_pdf):

    return a_lem_vect

import tempfile
import random
from new_chatbot import*

def generate_product_name(temp_file):
    # Read the product name from the temporary file
    with open(temp_file, 'r') as f:
        product_name = f.read().strip()

    # Generate a random product name if no product name is found in the temporary file
    if not product_name:
        product_names = ["Samsung1000", "Toaster", "Microwave", "Fridge", "Washing Machine", "Dishwasher"]
        product_name = random.choice(product_names)

    return product_name

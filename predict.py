def predict(image):
    uploaded_model = model.load('pathe_to_the_model')

    object_prediction = uploaded_model.predict(image)

    return object_prediction

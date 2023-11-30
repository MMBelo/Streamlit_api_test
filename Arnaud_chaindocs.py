from functions import *


def file_selection(object_name):

    selected_file = object_name.pdf

    manual_vectorized = vect_pdf(selected_file)

    manual_lematized = lem_vect_pdf(manual_vectorized)

    return manual_lematized


def vect_pdf(manual_pdf):

    return manual_pdf_vectorized

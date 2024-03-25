import pytest
from ..utils.functions import remove_leading_numbers  # Make sure to replace 'your_module' with the actual name of your Python file containing the function

def test_with_number_and_period():
    assert remove_leading_numbers("21. Sipas këtij neni, anulohen kontratat e pavlefshme.") == "Sipas këtij neni, anulohen kontratat e pavlefshme."

def test_with_number_no_period():
    assert remove_leading_numbers("5 Sipas këtij neni, anulohen kontratat e pavlefshme.") == "Sipas këtij neni, anulohen kontratat e pavlefshme."

def test_no_leading_number():
    assert remove_leading_numbers("Paragraf pa numra.") == "Paragraf pa numra."

def test_empty_string():
    assert remove_leading_numbers("") == ""

def test_only_numbers():
    assert remove_leading_numbers("12345") == ""

def test_numbers_with_multiple_spaces():
    assert remove_leading_numbers("2023.    Paragraf interesant") == "Paragraf interesant"

def test_leading_zeros():
    assert remove_leading_numbers("009. Pragraf interesant") == "Pragraf interesant"

# Testing with a negative number
def test_negative_number():
    assert remove_leading_numbers("-25 Fillim i pa-parashikuar") == "-25 Fillim i pa-parashikuar"

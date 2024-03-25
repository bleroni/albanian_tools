import pytest
from ..utils.functions import replace_numbers_with_albanian_text

# Test with a single number
def test_single_number():
    assert replace_numbers_with_albanian_text("Neni 217") == "Neni dyqind e shtatëmbëdhjetë", "Single number replacement failed"

# Test with multiple numbers
def test_multiple_numbers():
    assert replace_numbers_with_albanian_text("Sipas kësaj, neni 17 dhe paragrafi 97, nuk i plotësojnë kushtet.") == "Sipas kësaj, neni shtatëmbëdhjetë dhe paragrafi nëntëdhjetë e shtatë, nuk i plotësojnë kushtet.", "Multiple numbers replacement failed"

# Test with no numbers
def test_no_numbers():
    assert replace_numbers_with_albanian_text("No numbers here!") == "No numbers here!", "Failed when no numbers are present"

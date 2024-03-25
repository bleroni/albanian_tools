import pytest
from ..utils.functions import integer_to_albanian_text_converter

# Test a simple number
def test_simple_number():
  assert integer_to_albanian_text_converter(19) == "nëntëmbëdhjetë", "Failed for 19"

# Test a number with a zero in the tens place
def test_more_complicated_number():
  assert integer_to_albanian_text_converter(717) == "shtatëqind e shtatëmbëdhjetë", "Failed for 717"

# Test a number with a zero in the units place
def test_with_zero():
  assert integer_to_albanian_text_converter(808) == "tetëqind e tetë", "Failed for 808"  

# Test for out of range numbers
def test_out_of_range():
  assert integer_to_albanian_text_converter(1000) == "Number out of range", "Failed for 1000"
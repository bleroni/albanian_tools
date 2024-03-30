# Albanian Tools
## Installation 
```python
pip install albanian_tools
```

## Usage

There are three main functions: `remove_leading_numbers`, `replace_numbers_with_albanian_text`, and `integer_to_albanian_text_converter`.

```python
from albanian_tools import AlbanianTools

albanian_tool = AlbanianTools()

# remove_leading_numbers
text_1 = "913. Paragraf interesant" # Returns "Paragraf interesant"
text_1_text_numbers = albanian_tool.remove_leading_numbers(text_1)
print(f"remove_leading_numbers: {text_1_text_numbers}")

# replace_numbers_with_albanian_text
text_2 = "Neni 217 kalon tutje." # Returns "Neni dyqind e shtatëmbëdhjetë kalon tutje."
text_2_text_numbers = albanian_tool.replace_numbers_with_albanian_text(text_2)
print(f"replace_numbers_with_albanian_text: {text_2_text_numbers}")

# integer_to_albanian_text_converter
integer_example = 717 # Returns "shtatëqind e shtatëmbëdhjetë"
integer_example_text_number = albanian_tool.integer_to_albanian_text_converter(integer_example)
print(f"integer_to_albanian_text_converter: {integer_example_text_number}")

# Random number in Albanian
print(f"random_albanian_number: {albanian_tool.random_albanian_number()}")

# Random Albanian name
print(f"random_albanian_name: {albanian_tool.random_albanian_name()}")
```
# Albanian Tools

## Installation 
```python
pip install albanian_tools
```

## Usage

There are three main functions: `remove_leading_numbers`, `replace_numbers_with_albanian_text`, and `integer_to_albanian_text_converter`.

```python
import albanian_tools

# remove_leading_numbers
text_1 = "913. Paragraf interesant"
text_1_text_numbers = albanian_tools.remove_leading_numbers(text_1) # Returns "Paragraf interesant"

# replace_numbers_with_albanian_text
text_2 = "Neni 217 kalon tutje."
text_2_text_numbers = albanian_tools.replace_numbers_with_albanian_text(text_2) # Returns "Neni dyqind e shtatëmbëdhjetë kalon tutje."

# integer_to_albanian_text_converter
integer_example = 717
integer_example_text_number = albanian_tools.remove_leading_numbers(integer_example) # Returns "shtatëqind e shtatëmbëdhjetë"
```

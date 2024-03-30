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
text_1 = "913. Paragraf interesant" # Returns "Paragraf interesant"
text_1_text_numbers = albanian_tools.remove_leading_numbers(text_1)

# replace_numbers_with_albanian_text
text_2 = "Neni 217 kalon tutje." # Returns "Neni dyqind e shtatëmbëdhjetë kalon tutje."
text_2_text_numbers = albanian_tools.replace_numbers_with_albanian_text(text_2)

# integer_to_albanian_text_converter
integer_example = 717 # Returns "shtatëqind e shtatëmbëdhjetë"
integer_example_text_number = albanian_tools.integer_to_albanian_text_converter(integer_example)
```

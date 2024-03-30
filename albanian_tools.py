from .utils.functions import integer_to_albanian_text_converter, replace_numbers_with_albanian_text, remove_leading_numbers

class AlbanianTools:
    def random_albanian_name(self) -> str:
        return "Filan Fisteku test"
    
    def remove_leading_numbers(self, text: str) -> str:
        return remove_leading_numbers(text)
    
    def integer_to_albanian_text_converter(self, decimal_integer: int) -> str:
        return integer_to_albanian_text_converter(decimal_integer)
    
    def replace_numbers_with_albanian_text(self, text: str) -> str:
        return replace_numbers_with_albanian_text(text)
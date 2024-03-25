from utils.functions import integer_to_albanian_text_converter, replace_numbers_with_albanian_text

class AlbanianTools:
    def integer_to_albanian_text_converter(self, decimal_integer: int) -> str:
        return integer_to_albanian_text_converter(decimal_integer)
    
    def replace_numbers_with_albanian_text(self, text: str) -> str:
        return replace_numbers_with_albanian_text(text)
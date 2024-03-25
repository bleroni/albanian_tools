import re

def remove_leading_numbers(s):
    # Pattern to match numbers (with optional period) at the beginning of the string and optional spaces after
    pattern = r'^\d+\.?\s*'

    return re.sub(pattern, '', s)

def replace_numbers_with_albanian_text(text: str) -> str:
    # Use a regular expression to match numbers between 0 and 999
    pattern = r'\b\d{1,3}\b'
    
    # Define a function that will be used for substitution
    def replacement(match):
        # Convert the matched string to an integer
        number = int(match.group(0))
        if number >= 1000:
            return "Number out of range"
        # Return the string representation of the custom function's result
        return integer_to_albanian_text_converter(number)
    
    # Use re.sub with the replacement function to replace numbers
    return re.sub(pattern, replacement, text)

def integer_to_albanian_text_converter(number: int) -> str:
    if number < 0 or number >= 1000:
        return "Number out of range"

    units = ["", "një", "dy", "tre", "katër", "pesë", "gjashtë", "shtatë", "tetë", "nëntë"]
    tens = ["", "dhjetë", "njëzet", "tridhjetë", "katërdhjetë", "pesëdhjetë", "gjashtëdhjetë", "shtatëdhjetë", "tetëdhjetë", "nëntëdhjetë"]
    hundreds = ["", "njëqind", "dyqind", "treqind", "katërqind", "pesëqind", "gjashtëqind", "shtatëqind", "tetëqind", "nëntëqind"]

    if number == 0:
        return "zero"

    num_hundreds = number // 100
    num_tens = (number % 100) // 10
    num_units = number % 10

    result = []

    if num_hundreds > 0:
        result.append(hundreds[num_hundreds])
        if num_tens > 0 or num_units > 0:
            result.append("e")

    if num_tens > 0:
        result.append(tens[num_tens])
        if num_units > 0 and num_tens > 1:
            result.append("e")

    if num_units > 0:
        # Special case for 11-19
        if num_tens == 1:
            correct_number = f"{units[num_units]}mbëdhjetë"
            result[-1] = correct_number
        else:
            result.append(units[num_units])

    return ' '.join(result).strip()



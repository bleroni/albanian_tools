def integer_to_albanian_text_converter(any_number: int) -> str:
    if any_number < 0 or any_number >= 1000:
        return "Number out of range"

    units = ["", "një", "dy", "tre", "katër", "pesë", "gjashtë", "shtatë", "tetë", "nëntë"]
    tens = ["", "dhjetë", "njëzet", "tridhjetë", "katërdhjetë", "pesëdhjetë", "gjashtëdhjetë", "shtatëdhjetë", "tetëdhjetë", "nëntëdhjetë"]
    hundreds = ["", "njëqind", "dyqind", "treqind", "katërqind", "pesëqind", "gjashtëqind", "shtatëqind", "tetëqind", "nëntëqind"]

    if any_number == 0:
        return "zero"

    num_hundreds = any_number // 100
    num_tens = (any_number % 100) // 10
    num_units = any_number % 10

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



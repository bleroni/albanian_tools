from classes.albanian_tools import AlbanianTools

albanian_tools = AlbanianTools()

# text_string = 'Sipas kësaj, neni 17 dhe paragrafi 97, nuk i plotësojnë kushtet.'
# text_string = 'Janë mbjellur rreth 1000 e 52 hektarë'
# print(text_string)

# modified_text = albanian_tools.replace_numbers_with_albanian_text(text_string)
# print(modified_text)


# albanian_text = albanian_tools.integer_to_albanian_text_converter(217)
# print(albanian_text)
# Testing the examples provided
print(albanian_tools.integer_to_albanian_text_converter(451))
print(albanian_tools.integer_to_albanian_text_converter(19))
print(albanian_tools.integer_to_albanian_text_converter(717))
print(albanian_tools.integer_to_albanian_text_converter(888))
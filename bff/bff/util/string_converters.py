def snake_to_pascal(snake_case):
    """
    Convert a snake_string to a PascalString.
    Converts the given string in snake case to Pascal case. Example:
        example_variable -> ExampleVariable
    """
    if type(snake_case) is not str:
        raise TypeError("Can't convert case. snake_case is a non-string variable.")

    words_to_convert = snake_case.split('_')
    pascal_case = ''
    for word in words_to_convert:
        word = word[0].upper() + word[1:]
        pascal_case = pascal_case + word

    return pascal_case

"""
# These should convert to the value in the comments.
print(snake_to_pascal("this_is_a_snake")) # ThisIsASnake
print(snake_to_pascal("ThisIsAlreadyPascal")) # ThisIsAlreadyPascal
print(snake_to_pascal("hahaImInCamel")) # HahaImInCamel
print(snake_to_pascal("Spongebob was here.")) # Spongebob was here.
"""
"""
# These should throw TypeError exceptions.
print(snake_to_pascal(None))
print(snake_to_pascal(True))
print(snake_to_pascal(False))
"""

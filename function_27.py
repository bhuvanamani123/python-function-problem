"""changeCharCase : A method which accepts a char
as intput and returns a char whose case if changed."""

def change_char_case(char):
    return char.lower() if char.isupper() else char.upper()

char_input = input("Enter a character: ")

result = change_char_case(char_input)

print(result)

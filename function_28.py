"""28. isDigit : Given a char as input, return true if it is a
digit (i.e. between 0 to 9)"""

def is_digit(char):
    return char.isdigit()

char_input = input("Enter a character: ")

result = is_digit(char_input)

print(result)

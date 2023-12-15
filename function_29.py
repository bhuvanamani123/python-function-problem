""" MiddleChar : Given three chars as input, return the
char that would come in the middle if the chars were
arranged in order. Note that > operator can be used for
chars.
"""




def middle_char(char1, char2, char3):
    chars = [char1, char2, char3]
    chars.sort()
    return chars[1]


char1 = input("Enter the first character: ")
char2 = input("Enter the second character: ")
char3 = input("Enter the third character: ")

result = middle_char(char1, char2, char3)

print(result)

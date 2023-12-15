"""AddDigitNumbers : Given three digits as input,
create a 4 digit number out of each input in which all
the digits are the same and then add all the 3
numbers and return the value. (ip: 1,2,3 op:
1111+2222+3333)."""



def add_digit_numbers(digit1, digit2, digit3):
    num1 = int(f"{digit1}{digit1}{digit1}{digit1}")
    num2 = int(f"{digit2}{digit2}{digit2}{digit2}")
    num3 = int(f"{digit3}{digit3}{digit3}{digit3}")
    return num1 + num2 + num3

digit1 = int(input("Enter the first digit: "))
digit2 = int(input("Enter the second digit: "))
digit3 = int(input("Enter the third digit: "))

result = add_digit_numbers(digit1, digit2, digit3)

print(result)

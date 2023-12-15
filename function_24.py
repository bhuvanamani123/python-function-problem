"""Multiple37 : Given a number n, return true if it is
divisible by either 3 or 7."""
def is_multiple_of_3_or_7(num):
    return num % 3 == 0 or num % 7 == 0

number_input = int(input("Enter a number: "))

result = is_multiple_of_3_or_7(number_input)

print(result)

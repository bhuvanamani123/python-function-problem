"""SumOf4Digits : Given a number as input, compute
the sum of its last 4 digits. Assume that the number
has at least 4 digits."""

def sum_of_4digits(number):
    return sum(map(int, str(number)[-4:]))

input_number = int(input("Enter a number with at least 4 digits: "))

result = sum_of_4digits(input_number)

print(result)

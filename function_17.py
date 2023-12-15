"""sum2Digit : Given a 2 digit number as input,
compute the sum of its digits. Assume that the
number has 2 digits. Eg : if 12 is given as input then
op should be 3."""


def sum2Digit(number):
   
    tens_place = number // 10
    ones_place = number % 10
    digit_sum = tens_place + ones_place
    return digit_sum
digit_number = 5683
result = sum2Digit(digit_number)
print(result)


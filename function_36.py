#reverse3 : Given a 3 digit number as input, reverse it

def reverse_digit(number):
    if 99< number<1000:
        reverse = int(str(number)[::-1])
        return reverse
    else:
        return"enter valid number"
values = int(input("enter a 3-digits number: "))
values_1 = reverse_digit(values)
print(values_1)




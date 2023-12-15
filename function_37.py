"""perfectNumber: A perfect number is a positive
integer that is equal to the sum of its factors. For
example, 6 is a perfect number because 6=1+2+3; but
24 is not perfect because 24<1+2+3+4+6+8+12.
Given a number n, the objective is find out whether it
is a perfect number or not."""

def perfect_number(number):
    if number <=0:
        return False
    sum_values = sum(i for i in range(1,number)if number%i==0)
    return sum_values == number
num = 6 
values_1 = perfect_number(num)
if values_1:
    print("perfect value")
else:
    print("non prefect values")
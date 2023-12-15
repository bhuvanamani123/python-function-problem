# Write a function that accepts an integer and returns
#the digits repeated twice. (ip: 12, op:1212).


def digits_repated(integer):
    return int(str(integer)+str(integer))
number = 12
values_1 = digits_repated(number)
print(values_1)
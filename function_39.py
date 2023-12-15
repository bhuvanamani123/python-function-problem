# A function accepts a number as input and returns a
#string filled with random integers as many times as
#the input.

import random
def random_integer(number):
    return "".join(str(random.randint(0,9)) for i in range(number))
num = 6
print(random_integer(num))

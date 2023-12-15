"""function accepts a number as input and returns a
string filled with natural numbers as many as the
input."""


def natural_number(number):
  return "".join(str(i) for i in range(1,number+1))
num = 10
print(natural_number(num))
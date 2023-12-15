"""MakeDecimal : Given 3 digits a,b and c as input,
return a double of the form a.bc."""

def make_decimal(a,b,c):
    num = a*100+b*10+c*0.1
    return num
digit_a = 200
digit_b = 100
digit_c = 369

result = make_decimal(digit_a, digit_b, digit_c)
print(result)
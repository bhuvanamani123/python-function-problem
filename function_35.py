"""Blackjack : Given 2 int values greater than 0, return
whichever value is nearest to 21 without being
greater than 21. Return -1 if the values are greater
than 21. Also return -2 if both the values are same
and less or equal to 21"""

def blackjack(a,b):
    if a>21 and b>21:
       return -1
    elif a>21:
        return b
    elif b>21:
        return a
    elif a==b and a<=21:
        return -2
    else:
        if abs(21-a) < abs(21-b):
            return a
        else:
            return b
value1 = int(input("enter the first value: "))
values2 = int(input("enter the second  value: "))       

result = blackjack(value1,values2)
print(result)          
     

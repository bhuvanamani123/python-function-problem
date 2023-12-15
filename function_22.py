"""""AreaOfSquare : You have been given 4 inputs
x1,y1,x2 and y2. The points (x1,y1) and (x2,y2)
represent the end points of the diagonal of a square.
Return the area of the square."""


def area_of_square(x1, y1, x2, y2):
    side_length = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    area = side_length**2
    return area
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

result = area_of_square(x1, y1, x2, y2)

print(result)

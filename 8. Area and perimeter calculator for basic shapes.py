x = str(input("To find area and perimeter for square enter s,\n for triangle enter t,\n for rectangle enter r,\n for circle enter c: "))

#for square
if x == "s":
    a = float(input("Enter the length of any side of a square in cm: "))
    area = a**2
    perimeter = 4*a
    print("Area of square = ", area)
    print("Perimeter of square = ", perimeter)

#for rectangle
elif x == "r":
    l = float(input("Enter the length of rectangle in cm: "))
    w = float(input("Enter the width of rectangle in cm: "))
    area = l*w
    perimeter = 2*(l+w)
    print("Area of rectangle = ", area)
    print("Perimeter of rectangle = ", perimeter)

#for triangle
elif x == "t":
    a = float(input("Enter the length of side a of triangle in cm: "))
    b = float(input("Enter the length of side b of triangle in cm: "))
    c = float(input("Enter the length of base of triangle in cm: "))
    ph = float(input("Enter the perpendicular height of triangle in cm: "))
    area = (1/2) * ph * c
    perimeter = a + b + c
    print("Area of triangle = ", area)
    print("Perimeter of tirangle = ", perimeter)

#for circle
else:
    radius = float(input("Enter the radius of the circle in cm: "))
    pi = 3.14
    area = pi* (radius**2)
    circumference = 2*pi*radius
    print("Area of circle = ", area)
    print("Perimeter/circumference of circle = ", perimeter)






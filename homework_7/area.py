import math
def rectangle():
    """
    This function calculates the square of ​​a rectangle,
    parameters:
        lenght of rectangle's side
    """
    len_of_side = float(input("Enter a lenght of your rectangle's side: "))
    return f"The square of your rectangle is {math.pow(len_of_side, 2)}"
def triangle():
    """
    This function calculates the square of ​​a triangle,
    parameters:
        lenght of triangles's base
        lenght of triangle's height
    """
    base = float(input("Enter a lenght of your triangle's base: "))
    height = float(input("Enter a lenght of your triangle's height: "))
    return f"The square of your rectangle is {(base*height)/2}"
def circle():
    """
    This function calculates the square of ​​a circle,
    parameters:
        radius of a circle
    """
    radius = float(input("Enter a radius of your circle: "))
    return f"The square of your circle is {math.pi*math.pow(radius, 2)}"
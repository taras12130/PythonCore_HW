# Write a program that calculates the square of ​​a rectangle, triangle and circle 
# (write three functions to calculate the square, and call them in the main program depending on the user's choice).

def square_of_rectangle():
    """
    This function calculates the square of ​​a rectangle,
    parameters:
        lenght of rectangle's side
    """
    len_of_side = float(input("Enter a lenght of your rectangle's side: "))
    return f"The square of your rectangle is {len_of_side**2}"
def square_of_triangle():
    """
    This function calculates the square of ​​a triangle,
    parameters:
        lenght of triangles's base
        lenght of triangle's height
    """
    base = float(input("Enter a lenght of your triangle's base: "))
    height = float(input("Enter a lenght of your triangle's height: "))
    return f"The square of your rectangle is {(base*height)/2}"
def square_of_circle():
    """
    This function calculates the square of ​​a circle,
    parameters:
        radius of a circle
    """
    PI = 3,14
    radius = float(input("Enter a radius of your circle: "))
    return f"The square of your circle is {PI*radius**2}"
answer = input("This program can calculate a square of rectangle, triangle and circle, choose one: ")
if "rectangle" in answer.lower().split():
    print(square_of_rectangle())
elif "triangle" in answer.lower().split():
    print(square_of_triangle())
elif "circle" in answer.lower().split():
    print(square_of_circle())
else:
    print("You need to choose one of those three: rectangle, triangle or circle")
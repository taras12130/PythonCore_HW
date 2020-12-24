# Create a polygon class and a rectangle class 
# that inherits from the polygon class and finds the square of rectangle. 

class Polygon:
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side

class Rectangle(Polygon):
    def square(self):
        return f"The square of your rectangle is {self.first_side * self.second_side}"

obj = Rectangle(4, 2)
print(obj.square())
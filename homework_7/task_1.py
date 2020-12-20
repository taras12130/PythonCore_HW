import area
answer = input("This program can calculate a square of rectangle, triangle and circle, choose one: ")
if "rectangle" in answer.lower().split():
    print(area.rectangle())
elif "triangle" in answer.lower().split():
    print(area.triangle())
elif "circle" in answer.lower().split():
    print(area.circle())
else:
    print("You need to choose one of those three: rectangle, triangle or circle")
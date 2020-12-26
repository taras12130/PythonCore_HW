# Write a program that prompts the user to enter their age, and then displays a message 
# stating whether the age is even or odd. The program must provide the ability to enter a negative number, 
# and in this case generate an exception. 
# The master code should call a function that processes the information entered. 

def age_validation(age):
    if age < 0:
        raise ValueError("Age must be a positive number!")
    if age % 2 == 0:
        return "Your age is even"
    else:
        return "Your age is odd"

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError as e:
        print("Your age is not correct!", e)
        
print(age_validation(age))
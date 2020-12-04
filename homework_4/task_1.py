# Write a script that will calculate the factorial of the entered number  without using recursion.
number = int(input("Enter a number: "))
if number < 0:
    print("Wrong number!")
else:
    fact = 1
    i = 1
    while i <= number:
        fact = fact * i
        i += 1
    print(f"{number}! = {fact}")
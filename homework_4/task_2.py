# Create a list that contains elements of integer type,
# then use the loop to change the type of these elements to a floating type. 
try:
    list_of_int_numbers = [int(input(f"Enter a {i + 1} number: ")) for i in range(int(input("How many numbers in your list? ")))]
    list_of_float_numbers = []
    print(f"Your list is {list_of_int_numbers}")
    for i in list_of_int_numbers:
        list_of_float_numbers.append(float(i))
    print(f"Your list with float numbers is: {list_of_float_numbers}")
except ValueError:
    print("Your number must be integer!")
# Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function). 

def largest_num(num1, num2):
    """
    This function returns the largest number of two numbers
    """
    if num1 == num2:
        return num1
    else:
        if num1 > num2:
            return num1
        else:
            return num2
print(largest_num(5, 7))
print(largest_num.__doc__)
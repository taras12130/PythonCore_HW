# Write a program that analyzes the entered number and,
# depending on the number, gives the day of the week that corresponds to this number (1 is Monday, 2 is Tuesday, etc.).
# Take into account cases of entering numbers from 8 and more, as well as cases of entering non-numerical data. 

while True:
    try:
        number_of_day = int(input("Enter a number of a day of week: "))
        days_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7:"Sunday"}
        print(days_of_week[number_of_day])
        break
    except ValueError as e:
        print("It is not a number!", e)
    except KeyError as e:
        print("Your number must be from 1 to 7!", e)
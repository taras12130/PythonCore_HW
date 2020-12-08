# Задано чотирицифрове натуральне число. 
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число
try:
    num = int(input("Enter a four-digit number: "))
    num = str(num)
    if len(num)==4:
        mult = 1
        for i in range(4):
            mult = mult * int(num[i])
        print(f"Multiplication - {mult}")
        print(f"Reversed - {num[::-1]}")
        print(f"Sorted - {sorted(num)}")
    else:
        print("It must be four digits!")
except ValueError:
    print("It is not a number, try again!")
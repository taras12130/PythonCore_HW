# Print Fibonacci numbers up to the entered number n, 
# using cycles. 
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.) 
n = int(input("Enter a number: "))
if n <= 0:
    print("Wrong number!")
else:
    first = 0
    second = 1
    fibonacci = []
    while second <= n+1:
        fibonacci.append(str(first))
        fibonacci.append(str(second))
        first = first + second
        second = first + second
    print(f"Your fibonacci numbers: {' '.join(fibonacci)}")
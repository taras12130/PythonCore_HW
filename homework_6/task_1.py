# In the range from 1 to 10 determine 
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

div_by_2_nums = []
div_by_3_nums = []
other_nums = []
for i in range(1, 10):
    if i % 2 == 0:
        div_by_2_nums.append(str(i))
    elif i % 2 != 0:
        if i % 3 == 0:
            div_by_3_nums.append(str(i))
        else:
            other_nums.append(str(i))
print(f"Even numbers that are divisible by two: {' '.join(div_by_2_nums)}")
print(f"Odd numbers that are divisible by three: {' '.join(div_by_3_nums)}")
print(f"numbers that are not divisible by two and three: {' '.join(other_nums)}")
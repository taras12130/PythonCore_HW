# Will you make it?


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left < distance_to_pump:
        return False
    else:
        return True
print(zero_fuel(50, 25, 2))
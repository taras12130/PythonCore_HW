# Counting sheep...

def count_sheeps(sheep):
    counter = 0
    for i in sheep:
        if i:
            counter += 1
    return counter

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]             
print(count_sheeps(array1))
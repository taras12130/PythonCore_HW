# Convert boolean values to strings 'Yes' or 'No'.

def bool_to_word(boolean):
    if boolean == 1:
        return "Yes"
    else:
        return "No"
print(bool_to_word(True))
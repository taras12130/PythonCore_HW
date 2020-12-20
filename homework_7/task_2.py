# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re
password = "12130SSss"
if len(password) >= 6 and len(password) <= 16:
    if re.search("[a-z]", password):
        if re.search("[A-Z]", password):
            if re.search("[0-9]", password):
                if re.search("[$#@]", password):
                    print("Password is valid!")
                else:
                    print("There must be at least 1 special character ($, #, @)!")
            else:
                print("There must be at least 1 number!")
        else:
            print("There must be at least 1 upper-case letter!")
    else:
        print("There must be at least 1 lower-case letter!")
else:
    print("Your password's length must be from 6 to 16 characters!")
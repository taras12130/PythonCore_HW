def greetings():
    while True:
        login = input("Enter your login: ")
        if login == "First":
            return f"Hello, {login}!"
        else:
            print("Login is not correct, try again!")
print(greetings())
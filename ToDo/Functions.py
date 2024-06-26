def greet(name):
    upper_case = name.upper()
    return upper_case


user_name = input("Enter your name: ")
new_name = greet(user_name)
print(new_name)

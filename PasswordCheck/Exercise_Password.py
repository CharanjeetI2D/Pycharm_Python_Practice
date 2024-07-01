def strength(password):
    result = {}
    # Check length of password
    length = False
    if len(password) >= 8:
        length = True
    result["length"] = length

    # Check least one uppercase letter
    upper_case = False
    for i in password:
        if i.isupper():
            upper_case = True
    result["upper_case"] = upper_case

    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    result["digit"] = digit

    if all(result.values()):
        return "Password is Strong"
    else:
        return "Weak Password"


Check_Password = strength(input("Enter Password: "))
print(Check_Password)

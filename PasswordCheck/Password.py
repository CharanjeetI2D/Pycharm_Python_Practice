password = input("Enter a Password: ")

result = {}

# Checking the length of string >= 8
if len(password) >= 8:
    result["Length"] = True
else:
    result["Length"] = False

# Check if the string contains any digit
number = False
for i in password:
    if i.isdigit():
        number = True
result["Number"] = number

# Check if the string contains any alphabet
upper_char = False
for i in password:
    if i.isupper():
        upper_char = True
result["upper_char"] = upper_char

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")

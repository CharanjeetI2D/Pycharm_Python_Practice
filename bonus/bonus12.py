from bonus.converters14 import convert
from bonus.parsers14 import parsing

feet_inches = input("Please enter feet and inches: ")

parsed = parsing(feet_inches)
result = convert(parsed["feet"], parsed["inches"])
print(f"{parsed['feet']} feet and {parsed['inches']} inches is {result} meters.\n")

print(result)

if result < 1:
    print("Kid is too small. ")
else:
    print("Kid can use the slide. ")


try:
    width = float(input("Please enter width: "))
    height = float(input("Please enter height: "))

    if width == height:
        exit('Width and height cannot be the same for rectangle.')

    result = width * height
    print(result)
except ValueError:
    print("Please enter only numbers")


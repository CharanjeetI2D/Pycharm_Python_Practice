feet_inches = input("Please enter feet and inches: ")


def convert(feet_inches):
    split_feet_inches = feet_inches.split(" ")
    feet = float(split_feet_inches[0])
    inches = float(split_feet_inches[1])

    meter = feet * 0.3048 + inches * 0.0254
    return meter


result = convert(feet_inches)

if result < 1:
    print("Kid is too small. ")
else:
    print("Kid can use the slide. ")


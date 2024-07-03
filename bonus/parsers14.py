def parsing(feet_inches):
    split_feet_inches = feet_inches.split(" ")
    feet = float(split_feet_inches[0])
    inches = float(split_feet_inches[1])
    return {"feet": feet, "inches": inches}

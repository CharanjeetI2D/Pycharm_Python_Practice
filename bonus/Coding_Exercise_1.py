import random

lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

random_number = random.randrange(lower_bound, upper_bound)

print(random_number)

import random

names = ["atharv", "amit", "sumit", "sonali", "aditi", "bunny", "johnny", "Sunny"]
length = len(names)
random_pay = random.randint(0, length-1)
person_pay = names[random_pay]
print(person_pay, "Will pay for today\'s mill")

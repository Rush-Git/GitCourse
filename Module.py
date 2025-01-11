from random import randint

no_of_gallon = randint(10, 25)
miles_driven = randint(200, 400)
print(no_of_gallon)
print(miles_driven)
mile_per_gallon = miles_driven // no_of_gallon
print(mile_per_gallon)

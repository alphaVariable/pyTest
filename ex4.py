# ek sau caarein
cars = 100
#kitne bande baith sakte hege ek car mein
space_in_a_car = 4.0
# Kitne driver hainge apne paas
drivers = 30
# kitne bande le ke jaane hain saath mein. Pta nai driver ko gina hai author ne ya nai
passengers = 90
# Kitni caaron ko chalaya nai ja sakta
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print "There are:", cars, "cars available."
print "There are only:", drivers, "drivers available."
print "There will be:", cars_not_driven, "empty cars today."
print "We can transport:", carpool_capacity, "people today."
print "We need to put about:", average_passenger_per_car, "average passenger per car."
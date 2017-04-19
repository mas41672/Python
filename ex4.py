cars = 100          # the variable car is assigned the value 100 
space_in_a_car = 4  # the variable space_in_a_car is assigned the value 4 
drivers = 30        # the variable drivers is assigned the value 30
passengers = 90.0     # the variable 
cars_not_driven = cars - drivers # here the values of the variables cars
                                 # are subtracted
								 # 100 - 30
								 # the result 70 is saved in the variable cars_not_driven
cars_driven = drivers            # the additional variabel cars_driven makes the code more readable
carpool_capacity = cars_driven * space_in_a_car	# the variables cars_driven 
                                 # and apace_in_a_car are multiplied
average_passengers_per_car = passengers / cars_driven # this operation gives the avergage of passengers

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "Hey %s there." % "You"
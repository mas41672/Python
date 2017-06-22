people = 30 # init and declares variable
cars = 40 # init and declare variable car
buses = 15 # init and delare variable buses

if cars > people: # condition branch, test if bigger than statement is true
	print "We should take the cars." # previous greater-than statement is true, first line of block code executed
elif cars < people:# aditional continal branch is executed
	print "We should not take the cars."
else:              # if none of the if structure were met or true and executed only the else branch will be alternativley
	print "We can't decide."

	
if not(buses > cars):#not(
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "Alright, let's just take the buses."
elif people == buses:
	print "Test Test"
else:
	print "Fine, let's stay home then." 
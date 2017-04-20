#functions and variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):#fun def fun-name fun-arg fun-parentheses
	print "You have %d cheeses!" % cheese_count # print with str formatter
	print "You have %d boxes of crackers!" % boxes_of_crackers # print with str formatter
	print "Man that's enough for a party!" # print output
	print "Get a blanket.\n" # print output and new line
	
print "We can just give the function numbers directly:" # print output and newline
cheese_and_crackers(20, 30) # call function with number arguments

print "OR, we can use variables from our script:" 
amount_of_cheese = 10 # define input variables for function
amount_of_crackers = 50 # define input variables for function

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #call function with variables as arguments

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)  # calculation in the function call

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)# calculation in the funciton call


print "How old are you?", #print str
age = raw_input() # gets input into var 'age
print "How tall are you?", #prints question
height = raw_input() #input variable into height
print "How much do you weight?", #prints question
weight = raw_input() #inputs into into variable weight

print "So, you're %s old, %s tall and %s heavy." % (   # after the opening parenthesis start a new line
	age, height, weight)  #prints three strings with formaters

# question
# When my strings print out there's a u in front of them, as in u'35'.
That's how Python tells you that the string is Unicode. Use a %s format instead and you\'ll see ti printed like normal.



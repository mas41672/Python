x = "There are %d types of people." % 10 # def. of str 'x' with an intr format character -number inside str
binary = "binary"						 # def. of str 'binary'  
do_not = "don't"						 # def. of str do_not
y = "Those who know %s and those who %s." % (binary, do_not)  # def. of str y with two str format chr s - two strs inside a str

print x
print y

print "I said: %r." % x                  # string into strin through format char raw str d, also print - generas single-quotes
print "I also said: '%s'." % y           # print str with format chr str - str is put inside a str

hilarious = True						 # bool variable hilarious
joke_evaluation = "Isn't that joke so funny?! %r" #

print joke_evaluation % hilarious        # the print statement 

w = "This is the left side of..."
e = "a string with a right side."

print w + e                               # adding strings concatenates the strings - and therfore these are made longer			  
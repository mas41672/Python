i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num
	
	

def whilefun(border,increment):
	i = 0
	numbers =[]
	while i < border:
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now: ", numbers
		
		i = i + increment
		print "At the bottom: i is %d" % i

whilefun(10,2)
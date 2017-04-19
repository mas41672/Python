 # -- coding: utf- 8 - 
formatter = "%r %r %r %r"
# als prints are made of a str, percentage (%) and the input
print formatter % (1, 2, 3, 4) # prints ints into the raw str 
print formatter % ("one", "two", "three", "four") #3 # prints str into raw formatter
print formatter % (True, False, False, True) #  # the %r prin format accepts bool values
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (  # it is possible to write the parameters in the next line
	"I had this thing.",  #str with comma to avoid long line
	"That you could type up right.", #str with comma to avoid long line
	"But it didn't sing.",  #str with comma to avoid long line
	"So I said goodnight." #str with comma to avoid long line
)
#function and files
from sys import argv # import argv

script, input_file = argv # unpack argv

def print_all(f): # function prrint_all()
	print f.read() # read file Object f
	
def rewind(f):
	f.seek(0) # Move to new file position - offset from start of file since no argument precizing position

def print_a_line(line_count, f): # input: integer and 
	print line_count, f.readline() #number, next line from the file, as a string.
	
current_file = open(input_file) #file object curretn_file

print "First let's print the whole file:\n" # print

print_all(current_file) # call function print_all( ) - function used

print "Now let's rewind, kind of like a tape." # print

rewind(current_file) #move to the beguining of the file - function used

print "Let's print three lines:"

current_line = 1

print_a_line(current_line, current_file)  #funciton used

current_line += 1
print_a_line(current_line, current_file)  #function used

current_line += 1
print_a_line(current_line, current_file)  #function used




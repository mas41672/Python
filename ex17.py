from sys import argv   # import argv
from os.path import exists # import exists from os.path
#import matplotlib.pyplot as plt

script, from_file, to_file = argv # unpack into three string arguments

print "Copying from %s to %s" % (from_file, to_file) # print with to str format

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file) #exist with str argument
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()



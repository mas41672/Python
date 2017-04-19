# from sys import argv # import and show programmer details of code

# script, filename = argv # unpack argument variable into script and filename

# txt = open(filename) # generate 

# print "Here's your file %r: " % filename # print with raw string format
# print txt.read()          #invoke method read() on file object 'txt'
# txt.close()

print "Type the filename again:" # prompt user
file_again = raw_input("> ") # prompt input for file

txt_again = open(file_again) # function returns file object 'txt_again'

print txt_again.read() #in print - method read() is invoked on 'txt_again'
txt_again.close()
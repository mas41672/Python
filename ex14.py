from sys import argv # import

script, user_name = argv # unpack argv
prompt = '***>>>'  # define prompt

print "Hi %s, I'm the %s script." % (user_name, script) # prin with two str formatters
print "I'd like to ask you a few questions." # print str
print "Do you like me %s?" % user_name  # print with str format
likes = raw_input(prompt)  #raw inputs into variable likes

print "Where do you live %s?" % user_name # prints question with str format
lives = raw_input(prompt) # raw_input in str var lives

print "What kind of computer do you have?" # prints a question
computer = raw_input(prompt)  # raw_input int str var computer

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" % (likes, lives, computer) # this is pri statement with two raw strs input
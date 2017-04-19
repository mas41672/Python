# - -coding: utf- 8 -
 
myName = 'Zed A. Shaw'
myAge = 39 # not a lie
myHeight = 172.0# * 2,54 # cm
myWeight = 159 # lbs
myEyes = 'Blue'
myTeeth = 'White'
myHair = 'Brown'

print "Let's talk about %r." % myName
print "He's %r cm tall." % myHeight
print "He's %r pounds heavy." % myWeight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (myEyes, myHair)
print "His teeth are usually %r depending on the coffee." % myTeeth

# this line is tricky, try to get it exactly right
print "If I add %r, %r, and %r I get %d." % (myAge, myHeight, myWeight, myAge + myHeight + myWeight)
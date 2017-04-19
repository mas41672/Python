# -*- coding: utf-8 -*-
tabby_cat = """\tI'm tabbed in."""
persian_cat = """I'm split\non a line."""
backslash_cat = """I'm \\ \f  \\ cat."""

fat_cat = """
I'll do a list:\a
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat


#months = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
#pirnt months[2]
#print months[2].decode("utf-8")

months = [u"Januar", u"Februar", u"März", u"April", u"Mai", u"Juni",
          u"Juli", u"August", u"September", u"Oktober", u"November", u"Dezember"]

print months[2]

#while True:
#	for i in ["/","/","/","-","-","-","|","|","|","\\","\\","\\","|","|","|"]:
#		print "%s\r" % i,
text1 = "\nDirk"
text2 = '\nDirk'

inputString = "The writter of the tesxt is %s. The presenter of the text is also %s."
print inputString % ( text1, text2)
inputString2 = "The writter of the tesxt is %r. The presenter of the text is also %r."
print inputString2 % ( text1, text2)
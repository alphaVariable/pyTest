x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"

# a string was put inside of string here
y = "Those of us who know %s and those of us who %s." % (binary, do_not)
# a string was put inside of a string here
print "I said %r " % x
# a string was also put inside of a string here
print "I also said %s " % y

hilarious = False
# This is not a string going into a string, it's a boolean
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with the right side"
#Concateniation. Yay! :|
print w + e
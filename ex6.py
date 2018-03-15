x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"

y = "Those of us who know %s and those of us who %s." % (binary, do_not)
print "I said %r " % x
print "I also said %s " % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with the right side"

print w + e
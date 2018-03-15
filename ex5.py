name = "Vitalik Buterin"
age = 33
height = 170 #cm
height_in_inches = height * 0.393701
weight = 60 #kg
weight_in_stone = weight * 0.157473044
weight_in_pound = weight * 2.20462
eyes = "brown"
teeth = "brownish"
hair = "white"

print "Let's talk about my %s." % name
print "He's %d cm tall." % height
print "He's %d inches tall." % height_in_inches
print "He's %d kilo heavy. That's %r pounds or %s stones. Imagine being that heavy, lol." % (weight, weight_in_pound, weight_in_stone)
print "That's not too fucking heavy"
print "He's got %s eyes and %s hair" % (eyes, hair)
print "His teeth are usually %s, depending on the colour of the coffee" % teeth

#fucking octothorpe sign. Anyways, this line is supposed to be a bit heavy, try not to fuck it up, mate
print "If I add %d, %d and %d, I get %d" % (age, weight, height, age + weight + height)
print "If I multiply %r, %s, %s and %r, I get %r" % (eyes, age, weight, height, age * weight * height)
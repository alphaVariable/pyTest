from sys import argv

# script, first, second, third = argv

# print "The script is called: ", script
# print "Your first variable is called:", first
# print "Your second variable is called:", second
# print "Your third variable is called:", third

script, answer1, answer2 = argv

print "Thefile name, aka 'script' is called:", script
answer1 = raw_input("What the fuck is the capital of Australia? ")
answer2 = raw_input("What the fuck is the capital of Nigeria? ")
print "The capital of Australia is:", answer1
print "The capital of Nigeria is:", answer2
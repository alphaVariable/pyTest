from sys import argv

# script, first, second, third = argv

# print "The script is called: ", script
# print "Your first variable is called:", first
# print "Your second variable is called:", second
# print "Your third variable is called:", third

script, answer1, answer2 = argv

print "Thefile name, aka 'script' is called:", script
print "The capital of Australia is:", answer1
print "The capital of Nigeria is:", answer2
answer3 = raw_input("What's your name? ")
answer4 = int(raw_input("How old are you? "))
print "Congratulations %d year old %s, you may have answered the question correctly, I am not up to conditional statements just yet so enjoy it while you can" % (answer4, answer3)

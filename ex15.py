# Imports argv module
from sys import argv
# declares variables, filename to be opened
script, filename = argv

# opens the file entered by the user
txt = open(filename)
# prints the filename as confirmation to the user
print "Here's your file \033[0;31m%r\033[0m:" % filename
# Reads text (& prints to the terminal)
print txt.read()

print "type the filename again:"

file_again = raw_input('> ')

txt_again = open(file_again)
print txt_again.read()
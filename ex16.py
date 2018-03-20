from sys import argv

script, filename = argv

print "we are going to erase %r." % filename

print "If you don't want to do that, hit CTRL+C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
print("opening the file...")
target = open(filename, 'w')

print('Truncating the file. Goodbye!')

# target.truncate() #empties the file 
#Try what happens if you don't truncate the file.
#Did pretty much nothing, investigate further
#Read documentation and open in different modes to check whether or when truncate function is required
#Files open in 'r' mode by default

print "now I am going to have to ask you to submit three lines:"

line1 = raw_input("Line 1: ")
print "I am going to have to start taking notes."
target.write(line1)
target.write('\n')


line2 = raw_input("Line 2: ")
target.write(line2)
target.write('\n')

line3 = raw_input("Line 3: ")
target.write(line3)
# target.write('\n') # Probably not needed here

print "And finally we have to close it."

target.close()
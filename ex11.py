# print "How old are you?",
age = int(raw_input('How old are you? '))
# print "How tall are you?",
height = int(raw_input('How tall are you? '))
# print "How heavy are you?",
weight = int(raw_input('How heavy are you? '))

print "So you're %r years old %r cm tall and... jeesus fucking christ, %r kg heavy?" % (age, height, weight) #change %r to %s when on production
print (age + height) % weight #No complicated formula, just testing the modulus operator
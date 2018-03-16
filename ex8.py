formatter = "%s %r %r %r" #notice the difference between the output of %s (string) and %r (representative) 

print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
    'I had this thing',
    'That you could type upright, but you couldn\'t sit upright',
    'But it didn\'t sing.',
    'So I said goodnight.'
)
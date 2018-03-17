# Escape characters
tabby_cow = "\tI'm tabbed in." #\t
persian_cow = "I'm split\non a line." #\n
backslash_cow = "I'm \\ a \\ cow." #\\
fat_cow = '''
Here's a fucking list of what cows want:
\t*Love
\t*Interaction
\t*Not be killed\n\t*Grass
\t  *Peace
''' #Additional space on the last bullet point will get printed.    
print tabby_cow
print persian_cow
print backslash_cow
print fat_cow

# while True:
#     for i in ["/", "-", "|", "\\", "|"]:
#         print "%r\r" % i,
# I don't fucking understand this code just yet. Execute at your own peril. In case you get stuck, use control + C to terminate script processing. 

#Escapes in Python, and how to print the special characters
print '%r -> %s' % ('\\','\\')
print '%r -> %s' % ('\'','\'')
print '%r -> %s' % ("\"","\"")
print '%r -> %s' % ('\a','\a')
print '%r -> %s' % ('\b','\b')
print '%r -> %s' % ('\f','\f')
print '%r -> %s' % ('\n','\n')
s = u"\N{BLACK SPADE SUIT}"
print '%r -> %s' % (s,s)
print '%r -> %s' % ('\r','\r')
print '%r -> %s' % ('\thorizontal tab','\thorizontal tab')
print '%r -> %s' % (u'\u0908',u'\u0908') # 16 bit unicode characters are printed like this
print '%r -> %s' % (u'\U000003bb',u'\U000003bb') # 32 bit unicode characters are printed like this
print '%r -> %s' % ('\v','\v')
print '%r -> %s' % ('\176','\176') #octal characters
print '%r -> %s' % ('\x7a','\x7a') #hex characters
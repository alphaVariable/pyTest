# Escape characters
tabby_cow = "\tI'm tabbed in." #\t
persian_cow = "I'm split\non a line." #\n
backslash_cow = "I'm \\ a \\ cow." #\\
fat_cow = """
Here's a fucking list of what cows want:
\t*Love
\t*Interaction
\t*Not be killed\n\t*Grass
\t  *Peace
""" #Additional space on the last bullet point will get printed.    
print tabby_cow
print persian_cow
print backslash_cow
print fat_cow 
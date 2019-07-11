# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable *** (can't change)
# List: mutable *** (can change)

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

print(title)
print(sub_heading)
print(content)

# Equivalent to saying (unpacking) the following
# title = post[0]
# sub_heading = post[1]
# content = post[2]
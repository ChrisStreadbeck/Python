"""
post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

print(post[1::2]) # ETC
"""
#you can slice tuples just like you slice lists


post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

#when removing you're not technically adding to the original Tuple, you're creating new
#  tuples that don't have that data

# Removing elements from the end
"""
post = post[:-1]
print(post)
"""

#Removing from the beginning
"""
post = post[1:]
print(post)
"""

#Removing specific element (messy / not recommended)
"""
post = list(post)
post.remove('published')
post = tuple(post)
print(post)
"""
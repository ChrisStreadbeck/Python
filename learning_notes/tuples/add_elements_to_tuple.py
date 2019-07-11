post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# we can't add to a tuple, we need to leverage re-assignment to make the
#  variable store the new tuple set

print(id(post))

post += ('Published',)
#equivalent to: post = post + ('Published',)

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)

print(id(post))

#python uses an ID to represent different objects.  The different number
#  after we add 'published' shows that it's a different tuple entirely
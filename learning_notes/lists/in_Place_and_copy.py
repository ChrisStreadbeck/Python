tags = ['python', 'development', 'tutorials', 'code']

tags.extend(['Programming'])  #adds onto an existing list

#changes tags in place, but does not return a new value.  can't be stored in a new
#  variable (similar to sort)

print(tags)

new_tags = tags + ['editing'] #does add it to a list and store it into a new variable.
#  Most common because it allows you to leave the original list as is in case you use
#  it in another place in the program.

#best practice in general

print(new_tags)
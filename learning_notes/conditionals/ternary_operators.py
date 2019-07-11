role = 'admin'

auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)

#so when the value of 'role' is admin it can access, but if it's anything else it can't.
#So if you change it to: 

role = 'guest'

auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)

# then the guest is not allowed.abs

# Remember that readability is very important to Python.  We don't want Ternary Operators
#  that are very long because they become very difficult to read.  Ternary = True or False.
#   It can't be if, elif, else.
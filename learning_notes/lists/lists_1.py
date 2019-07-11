users = ['Kristine', 'Tiffany', 'Jordan']

print(users)

users.insert(0, 'Anthony') #inserts into the index number

print(users)

users.append('Ian') # adds it to the end of the list

print(users)

print(users[2]) # prints just the index chose

users[4] = 'Brayden' # replaces the value in the Index number and sets the value to the new string

print(users)

users.remove('Jordan') # removes the selected value, you have to know the value

print(users)

popped_user = users.pop() # removes the last item from the list, but doesn't just delete it
# from that list, instead it returns that as a saveable value.  It can also pop a variable
#  (nested list). whatever is last

print(popped_user)
print(users)

del users[0] # deletes the value in the index #

print(users)

mixed_list = [42, 10.3, 'Altuve', users] # can nest list with a variable, and lists can be
# multiple data types

#have to be careful with mixed variable type lists.  very easy to mess up functions that
#  run from that list. Generally betteer to keep data types seperate in nested lists.

print(mixed_list)
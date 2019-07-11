def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')
#adding "= variable" gives it a default value instead of throwing an EnvironmentError

#the defaults have to be the end of the list.abs

def some_function(collection = []):
  collection.append(1)
  return collection


print(some_function())
print(type(some_function))

#you don't want to put a mutable object in a default value.  It causes it to
#  be global instead of local, and if you call some_function() later it will
#  reference the results from before
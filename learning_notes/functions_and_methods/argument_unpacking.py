# args

def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')

# (*args) is best practice.  Technically a variable but it isn't clear if you use something else.  It is used when you don't know how many arguments there are in the data.

# the returned information is a Tuple.

def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')

# can use it in more complex situations as well. 

def greeting(**kwargs): #**key word arguments
  print(kwargs)



# **kwargs


greeting() #returns a dictionary
greeting(first = 'Kristine', last = 'Hudgens')

#a more commonplace example

def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting() #would print the guest because it has no args
greeting(first = 'Kristine', last = 'Hudgens')
#returns the first
#Lambda is a tool used to wrap up a smaller function and pass it to other functions

full_name = lambda first, last: f'{first} {last}'

def greeting(name):
  print(f'Hi there {name}')

greeting(full_name('kristine', 'hudgens'))

#so it's basically a short hand function (inline) and it allows the name to be called
#  simply later on in the second function.  

#Can be used with any type of code, but it's most commonly used for mathmatics

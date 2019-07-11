def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')
full_name('Taylor', 'Whatever')
full_name('Another', 'Name')

#very common function used in many Apps.

def auth(email, password):
  if email == 'kristine@hudgens.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('kristine@hudgens.com', 'asdf')
#also a very common authentication function with conditionals

def hundred():
  for num in range(1, 101):
    print(num)


hundred()
#prints all numbers from 1 to 100

def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(501)
#more complex version
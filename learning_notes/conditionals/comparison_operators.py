# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated - not used now)
# >  Greater than
# >= Greater than or equal to
# <= Less than
# <= Less than or equal to

#only looking for True or False. Equality/Ineq works for numbers and strings. > or < etc are only numbers.

username = "jonsnow"

if username == 'jonsnow':
  print("welcome")
else:
  print("you shall not pass!")

#or  

user_list = ['Kristine', 'Tiffany']
second_list = ['Jordan', 'Brayden']

if user_list == second_list:
  print('They match')
else:
  print('Nope..')
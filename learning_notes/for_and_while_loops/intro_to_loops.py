"""
Two Types

For in loops will run the # of times that there are elements
While loops will run until it hits the 'stop' that is programmed in.

"""

players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
  print(player)

# 'player' can be named anything as long as it's the same in both

for iterator in players:
  print(iterator)

#but 'players' is the initial variable
#The 'best practice' is if you have a plural name as the initial variable, you use
#  the singular. So player in players, or team in teams etc..

players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

#works the same for Tuples as lists  --^

# Dictionaries - how to loop
for player in players:
  print(player)

players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

# Need to grab the key and the value (key, value)
for position, player in players.items():
  print('Position', position)
  print('Player', player)
"""
usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'Sorry - but not sorry, {username}, you are the banned')
    continue
  else:
    print(f'{username} is allowed')
"""

usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)

#break is used more if you just want to find one thing and then be done
#  where continue will run it through everything.
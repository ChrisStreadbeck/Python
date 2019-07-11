teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

# print(teams[0])

angels = teams[1].get('angels', 'Team not found') #this is treating it like a list.  We knew it was a dictionary, so .get got the values we wanted and converts it to an actual list.

print(list(angels.values())[1])

#can use all the normal things when working with a list
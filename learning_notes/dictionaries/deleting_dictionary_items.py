teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

#del teams['angels'] #if you know 100% it exists this removes something permanently, errors if it doesn't exist



removed_team = teams.pop('red sox', 'Team not found') #only removes the value of the lookup, not the key, but without the values the key isn't functional. If the key isn't found it will store the "no team found" in the variable

print(removed_team)

print(teams)
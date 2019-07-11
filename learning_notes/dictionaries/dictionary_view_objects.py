players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

print(players.keys()) #brings back the keys as a dictionary view object.  You can't index this. You can loop through them. 

print(list(players.values())[1]) #can treat it as a list

# or

player_names = list(players.copy().values())

print(player_names) # with .copy you've got your own to modify however you need for your purposes 

team_groupings = teams.items()

print(team_groupings) #returns tuples

#you can loop through a dictionary view object

print(len(team_groupings)) # shows the number of keys as a tuple

print(list(team_groupings)[1]) #use just like a string

print(list(team_groupings)[1][1]) #can pull farther nested elements

print(list(team_groupings)[1][1][0]) # and even further
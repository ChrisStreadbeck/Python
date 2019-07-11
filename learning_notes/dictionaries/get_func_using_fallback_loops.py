teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

#If you try and pull something that isn't there
#featured_team = teams['mets'] 
#would throw an error


featured_team = teams.get('yankees', 'No featured team')
print(featured_team)

# teams.get('key', 'fallback)
# So if the 'key' isn't there, the fallback would be printed

featured_team = teams.get('diamondbacks', 'No featured team')
print(featured_team)

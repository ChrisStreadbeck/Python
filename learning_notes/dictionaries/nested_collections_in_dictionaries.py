teams = {
  'astros': ["Altuve", "Correa", "Bregman"],
  'angels': ["Trout", "Pujols"],
  'yankees': ["Judge", "Stanton"],
}
#astros here is a 'key'  The key is a string, anything that you can add to a string can be part of the key.

print(teams['astros']) # will print all values stored inside the identifier
print(teams['astros'][2]) #will print just the value stored inside index 2

#you can then store the information inside a variable

angels = teams['angels']
print(angels)

#allows you to manipulate the data without changing the dictionary

#You can also add a key to the dictionary.  

teams['red sox'] = ["Price", "Betts"]

print(teams)
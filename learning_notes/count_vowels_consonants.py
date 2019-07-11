vowels = (0)
consonants = (0)

data = input("Write a sentence, please.: ").strip().lower()

for letter in data:
  if letter in "aeiou":
    vowels = vowels + 1
  else:
    consonants = consonants + 1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))
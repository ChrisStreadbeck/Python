import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	w = w.loer()
	if word in data:
		return data[word]
	elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]
    elif w.upper() in data: #if user entered "nato" this will check for "NATO" as well.
    	return data[w.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		return "did you mean %s instead?" % get_close_matches(word(data.keys()))[0]
		answer = input("Y for yes, N for no. ").strip().lower()
			if answer == "y"
				return data[get_close_matches(word(data.keys()))[0]]
			elif answer == "n":
				return "That word doesn't exist. Please double check it."
			else: "We didn't understand your entry."
	else:
		return "That word doesn't exist. Please double check it."

word = input("Enter word: ")

output = (traslate(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)
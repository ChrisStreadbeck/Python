tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags) #remember 4 means index 0 to 3

last_item = tags[-1]  #shows last value item in the list
index_of_last_item = tags.index(last_item) #gives index of last item when paired with the line before. 

print(number_of_tags)
print(last_item)
print(index_of_last_item)

# List Sorting

#python sorts by the index order when imported into the list

print(tags)

tags.sort() #puts them in alphabetical

print(tags)

tags.sort(reverse=True) #inverse alphabetical order

print(tags)

totals = [234, 1, 543, 2345]

print(totals)

totals.sort() # sorts smallest number to biggest number

print(totals)

totals.sort(reverse=True) #inverse numerical order

print(totals)
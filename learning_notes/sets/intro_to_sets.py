#looks like a dictionary but lacks the keys. All elements have to be unique

tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

#nope
#print(tags[0])


# so to query info from a set you'd do the following:
query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
print(query_two)
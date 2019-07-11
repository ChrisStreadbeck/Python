sentence = 'The quick brown fox jumps over the lazy Dog'

word = 'dog'

if word in sentence:
  print("yes it was")
else:
  print("nope")

#will get nope, because Dog != dog

if word.lower() in sentence.lower():

#would be better to change all to lower case. 

nums = [1. 2. 3. 4]

if 3 in nums:
  print('yup')
else:
  print('nope')

#to check true or false
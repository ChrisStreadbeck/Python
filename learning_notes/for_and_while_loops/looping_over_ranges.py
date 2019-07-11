#ranges work like .get or slicing.  It goes up to the 2nd argument and stops right
#  before it.  So in example 1 it won't grab 10.

for num in range(1, 10):
  print(num)

for num in range(1, 10, 2):
  print(num)

#so in example 2 it will loop through the range of 1 to 10, and a step of 2 (aka every other)
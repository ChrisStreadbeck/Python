tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1] #skips first and last index, returns the rest
tag_range2 = tags[:-1:2] #takes every other starting at the first index
tag_range3 = tags[::-1] #reverses all values across the entire list

# .sort() looks at alphabetical etc, and ignores index - very different
#  from doing it by index value with [::-1]. Also, you can't store the
#  sorted value in a new variable, only in the original variable. Can't
#  assign to new while doing the .sort() command


print(tag_range)
print(tag_range2)
print(tag_range3)

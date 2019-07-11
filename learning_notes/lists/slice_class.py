tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

# = slice(index start, index stop, interval ~step)

print(slice_obj.start) #will give the index that it starts on -rarely used
print(slice_obj.stop)  #will give the index that it ends on -rarely used
print(slice_obj.step)  #will give the interval it's using - most useful

print(tags[slice_obj])
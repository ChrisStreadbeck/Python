#unpacking args
numbers = [1,2,3,4,5]
print(*numbers)

#packing **kwargs
def add(*numbers):
  total = 0
  for number in numbers:
    total = total + number
  return(total)

print(add(1,2,3,4,5))

# Packing *args
def about(name, age, likes):
  sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
  return sentence

dictionary = {"name":"bob", "age":"23", "likes":"python"}
print(about(**dictionary))


# Packing **kwargs
def foo(**kwargs):
  for key, value in kwargs.items():
    print("{}:{}".format(key, value))
  
foo(bob = "male", alice = "female", stan = "male", Jane = "female",)
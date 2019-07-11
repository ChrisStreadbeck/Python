name = input("What is your name?: ")
age = input("What is your age?: ")
city = input("What is your city?: ")
enjoy = input("What do you enjoy?: ")
string = "Your name is {} and you are {} years old.  You live in {} and you enjoy {}."
output = string.format(name, age, city, enjoy)
print(output)

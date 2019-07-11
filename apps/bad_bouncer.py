known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]

print(len(known_users))

while True:
  print("Hi! My name is Travis")
  name = input("What is your name?: ").strip().capitalize()

  if name in known_users:
    print("Hello, {}, how are you?".format(name))
    remove = input("Would you like to be removed from the system (y/n)?: ").lower()
    if remove == "y":
      known_users.remove(name)
      print("All Done!")
    else:
      print("Okay, I won't.")


  else:
    print("Hello, {}, I don't think I've met you yet.".format(name))
    add_question = input("Would you like to be added to the list? (y/n)? ").strip().lower()
    if add_question == "y":
      known_users.append(name)
      print("You are added.")
    else:
      print("Fine.. Be that way..")
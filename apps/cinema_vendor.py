from pprint import pprint
import time

films = {
  "Aladdin":      {"Minimum Age": 5, "tickets": 8},
  "Endgame":      {"Minimum Age":18, "tickets": 3},
  "Dark Phoenix": {"Minimum Age":13, "tickets":50},
  "Godzilla":     {"Minimum Age":13, "tickets": 9},
  "John Wick":    {"Minimum Age":18, "tickets": 1},
  "Pokemon":      {"Minimum Age": 5, "tickets":12},
}

while True:

  print(" ")
  pprint(films)
  print(" ")
  choice = input("Which movie would you like to see?: ").strip().title()

  if choice in films:
    age = int(input("How old are you?: ").strip())

    if age >= films[choice]["Minimum Age"]:
      
      num_seats = films[choice]["tickets"]

      if num_seats > 0:
        print("Enjoy the film!")
        films[choice]["tickets"] = films[choice]["tickets"] - 1
        print(" ")
      else: 
        print("Sorry, we are sold out.")
        print(" ")
    else:
      print("You are not old enough to see that yet.")
      print(" ")
  else:
    print("We don't have that film...")
    print(" ")
  time.sleep(2)
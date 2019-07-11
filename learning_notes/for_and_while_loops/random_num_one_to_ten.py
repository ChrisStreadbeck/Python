import random

nums = list(range(1, 10))

def guessing_game():
  while True:
    guess_range = random.choice(nums)
    guess = int(input("please guess a number between 1 and 10: "))
    if guess == guess_range:
      print("you got it!")
      return False
    else:
      print(f'No, {guess} is not the answer, please try again\n')

guessing_game()
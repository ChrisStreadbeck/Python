import random
import time
import os

def game_intro():
  os.system('cls')
  player_name = input("Hi there! What's your name? ")

  print(f'Well {player_name} get ready to wager on some Bingo!')
  time.sleep(4)
  os.system('cls')

  def print_rules():
    print("The rules are:")
    print("You will make a wager based on how many called numbers you think it will take to get Bingo.")
    print("If you are within 5 you'll get back 3x your wager,")
    print("if you are within 10 you'll get back 2x your wager,")
    print("and if you are over 10 away you'll lose your wager")
    print("You start with 50 units of wagering in your 'wallet'")
    time.sleep(2)
    player_ready = input("Are you ready? (yes or no)").strip().lower()
    if player_ready == 'yes':
      pass
    else:
      print_rules() 

  print_rules()
  os.system('cls')

game_intro()

wallet = 50
icon = "X"

while wallet >= 1:
  spacer_row = "--------------------------"
  b_column = []
  i_column = []
  n_column = []
  g_column = []
  o_column = []
  
  def print_board():
        
    while len(b_column) <= 5:
      for b in range(5):
        rand = random.randrange(1,15)
        if rand not in b_column:
          b_column.append(rand)
    while len(i_column) <= 5:
      for i in range(5):
        rand = random.randrange(16,30)
        if rand not in i_column:
          i_column.append(rand)
    while len(n_column) <= 4:
      for n in range(5):
        rand = random.randrange(31,45)
        if rand not in n_column:
          n_column.append(rand)
    while len(g_column) <= 5:
      for g in range(5):
        rand = random.randrange(46,60)
        if rand not in g_column:
          g_column.append(rand)
    while len(o_column) <= 5:
      for o in range(5):
        rand = random.randrange(61,75)
        if rand not in o_column:
          o_column.append(rand)

    header = "| B  | I  | N  | G  | O  |"
    row1 = f'| {b_column[0]} | {i_column[0]} | {n_column[0]} | {g_column[0]} | {o_column[0]} |'
    row2 = f'| {b_column[1]} | {i_column[1]} | {n_column[1]} | {g_column[1]} | {o_column[1]} |'
    row3 = f'| {b_column[2]} | {i_column[2]} | FS | {g_column[2]} | {o_column[2]} |'
    row4 = f'| {b_column[3]} | {i_column[3]} | {n_column[2]} | {g_column[3]} | {o_column[3]} |'
    row5 = f'| {b_column[4]} | {i_column[4]} | {n_column[3]} | {g_column[4]} | {o_column[4]} |'

    print()
    print(spacer_row)
    print(header)
    print(spacer_row)
    print(row1)
    print(spacer_row)
    print(row2)
    print(spacer_row)
    print(row3)
    print(spacer_row)
    print(row4)
    print(spacer_row)
    print(row5)
    print(spacer_row)
    print()

  called_list = []

  def num_gen():
    rand = random.randint(1,75)
    
    if rand not in called_list:
      called_list.append(rand)
    
      if rand in b_column:
        b_column[:] = ["X" if x==rand else x for x in b_column]
      elif rand in i_column:
        i_column[:] = ["X" if x==rand else x for x in i_column]
      elif rand in n_column:
        n_column[:] = ["X" if x==rand else x for x in n_column]
      elif rand in g_column:
        g_column[:] = ["X" if x==rand else x for x in g_column]
      elif rand in o_column:
        o_column[:] = ["X" if x==rand else x for x in o_column]

      if rand <= 15:
        return f'B{rand}'
      elif rand > 15 and rand <= 30:
        return f'I{rand}'
      elif rand > 30 and rand <= 45:
        return f'N{rand}'
      elif rand > 45 and rand <= 60:
        return f'G{rand}'
      elif rand > 60 and rand <= 75:
        return f'O{rand}'
    else:
      return num_gen()

  def is_victory(icon):
    if (b_column[0] == icon and b_column[1] == icon and b_column[2] == icon and b_column[3] == icon and b_column[4] == icon) or \
      (i_column[0] == icon and i_column[1] == icon and i_column[2] == icon and i_column[3] == icon and i_column[4] == icon) or \
      (n_column[0] == icon and n_column[1] == icon and n_column[2] == icon and n_column[3] == icon) or \
      (g_column[0] == icon and g_column[1] == icon and g_column[2] == icon and g_column[3] == icon and g_column[4] == icon) or \
      (o_column[0] == icon and o_column[1] == icon and o_column[2] == icon and o_column[3] == icon and o_column[4] == icon) or \
      (b_column[0] == icon and i_column[0] == icon and n_column[0] == icon and g_column[0] == icon and o_column[0] == icon) or \
      (b_column[1] == icon and i_column[1] == icon and n_column[1] == icon and g_column[1] == icon and o_column[1] == icon) or \
      (b_column[2] == icon and i_column[2] == icon and g_column[2] == icon and o_column[2] == icon) or \
      (b_column[3] == icon and i_column[3] == icon and n_column[3] == icon and g_column[3] == icon and o_column[3] == icon) or \
      (b_column[4] == icon and i_column[4] == icon and n_column[4] == icon and g_column[4] == icon and o_column[4] == icon) or \
      (b_column[0] == icon and i_column[1] == icon and g_column[3] == icon and o_column[4] == icon) or \
      (b_column[4] == icon and i_column[3] == icon and g_column[1] == icon and o_column[0] == icon):
      return True
    else:
      return False

  def play_round():
    called_number_count = 0
    
    def player_wager():
      player_wager.unit_wager = int(input(f'You currently have {wallet} units in your wallet.  How many would you like to bet on this round? '))
      if player_wager.unit_wager > wallet:
        print("You don't have that much in your wallet.")
        player_wager()
      else:
        print("Perfect.")
        return
    player_wager()

    rounds_wager = int(input("How many numbers do you think will be called before you get to BINGO? "))
    print("We will see if that was the right wager to make!")

    time.sleep(3)
    os.system('cls')

    print_board()

    while True:
      print(f'Numbers called so far: {called_number_count}')
      print("The number is: ")
      print(num_gen())
      time.sleep(.5)
      called_number_count = called_number_count + 1
      os.system('cls')
      print_board()
      if is_victory(icon):
        print("BINGO!")
        print("And that ends that round.")
        print(f'That took {called_number_count} numbers.')
        break

    if called_number_count > rounds_wager:
      rounds_math = called_number_count - rounds_wager
    else:
      rounds_math = rounds_wager - called_number_count

    print(f'You guessed that it would take {rounds_wager} numbers before we got a BINGO.  You were off by {rounds_math} on your guess.')

    if rounds_math <= 5:
      play_round.winnings = player_wager.unit_wager * 3
      print(f'Wow, you were so close! You made {play_round.winnings} this round')
      return play_round.winnings
    elif rounds_math <= 10:
      play_round.winnings = player_wager.unit_wager * 2
      print(f'Not bad! You made {play_round.winnings} this round')
      return play_round.winnings
    else:
      play_round.winnings = player_wager.unit_wager * -1
      print(f'Well, you lost {play_round.winnings} that round. Better luck next time.')
    return play_round.winnings

  play_round()

  wallet = wallet + play_round.winnings
  print("")
  print(f'you currently have {wallet} units in your wallet')
  print("")
  if wallet != 0:
    repeat = input("Would you like to go another round? (yes or no)").strip().lower()
    if repeat == "yes":
      pass
    elif repeat == "no":
      print("Thanks for playing!")
      break
  else:
    print("Well, you're broke. Come back soon!")
    break


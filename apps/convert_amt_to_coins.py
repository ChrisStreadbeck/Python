# Sample function : amountTocoins(46, [25, 10, 5, 1])
# Here 46 is the amount. and 25, 10, 5, 1 are coin types.
# Output : 25, 10, 10, 1

# need to find x in coins where x = [25, 10, 5, 1]

#what i found - works!!

# def change(number, coins_available, coins_so_far):
# 	if sum(coins_so_far) == number:
# 		yield coins_so_far
# 	elif sum(coins_so_far) > number:
# 		pass
# 	elif coins_available == []:
# 		pass
# 	else:
# 		for c in change(number, coins_available[:], coins_so_far+[coins_available[0]]):
# 			yield c
# 		for c in change(number, coins_available[1:], coins_so_far):
# 			yield c

# number = int(input("please write a number: "))
# coins = [25, 10, 5, 1]

# solutions = [s for s in change(number, coins, [])]
# print('Change would be:', min(solutions, key=len))

# ..but this is shorter..

def amount_to_coins(amount, coins):
  coins_list = []

  for coin in coins:
    while True:
      if amount - coin >= 0:
        coins_list.append(coin)
        amount -= coin
      else:
        break
  return coins_list

print(amount_to_coins(int(input("Please enter a number: ")), [25, 10, 5, 1]))
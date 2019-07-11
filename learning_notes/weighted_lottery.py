import numpy as np

def weighted_lottery(weights):
  container_list = []

  for (name, weight) in weights.items(): # for (key in weight)
    for _ in range(weight): # the underscore doesn't store the variable
      container_list.append(name) #
  return np.random.choice(container_list)

# The actual words in a lot of the variables don't matter.  'name' could be any variable as long as it's in both spots. 'container_list' as well, and 'weight'.  We control the naming of all the variables.


other_weights = {
  'winning': 20,
  'break_even': 40,
  'losing': 39,
  'jackpot': 1,
}

print(weighted_lottery(other_weights)) #weighted lottery points to the funtion
print(weighted_lottery(other_weights)) #other_weights is telling it which
print(weighted_lottery(other_weights)) #dictionary to pass into the code block
print(weighted_lottery(other_weights))
print(weighted_lottery(other_weights))
print(weighted_lottery(other_weights))

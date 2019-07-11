#Named Arguments
def full_name(first, last):
  print(f'{first} {last}')


full_name(first = 'Kristine', last = 'Hudgens')
full_name(last = 'Hudgens', first = 'Kristine')
#order doesn't matter in python, this is more explicit.  Rule of thumb
#  is to use named arguments if you have more than three being called in the function.
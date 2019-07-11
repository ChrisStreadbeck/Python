var_range = int(input("Enter a Number to set the upper range: "))

def fizzbuzz(upper):
  
  for num in range(1, upper): 
    
    if num != upper:
      if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
      elif num % 3 == 0:
        print('Fizz')
      elif num % 5 == 0:
        print('Buzz')
      else:
        print(num)


fizzbuzz(upper = var_range + 1)
# ----------------------
#without input

def fizzbuzz(upper):
  
  for num in range(1, upper): 
    
    if num != upper + 1:
      if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
      elif num % 3 == 0:
        print('Fizz')
      elif num % 5 == 0:
        print('Buzz')
      else:
        print(num)


fizzbuzz(100)
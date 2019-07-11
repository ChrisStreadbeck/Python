# My Solution (which worked)

from decimal import Decimal

def pretty_price(cost, p_number):
  cost = int(cost)
  
  if p_number % 1 == 0:
    n = p_number * round(Decimal(.01), 2)
  else:
    n = p_number
  
  output = cost + n
  return output


print(pretty_price(3.20, 99))
print(pretty_price(3.99, 0.20))
print(pretty_price(3.20, .95))
print(pretty_price(3, 95))
print(pretty_price(3, 2))
print("")



# Actual
def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01

    return int(gross_price) + extension


print(pretty_price(3.20, 99))
print(pretty_price(3.99, 0.20))
print(pretty_price(3.20, .95))
print(pretty_price(3, 95))
print(pretty_price(3, 2))
"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""
import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_prices = sorted(sale_prices)
num_of_sales = len(sorted_prices)
half_slice = math.floor(num_of_sales/2)

median = sorted_prices[half_slice:(half_slice + 1)]
print(median)



# first_sales = (sorted_prices[:len(sorted_prices) // 2])
# last_sales = (sorted_prices[:len(sorted_prices) // 2:-1])
# print(first_sales)
# print(last_sales)
# .sort() looks at alphabetical etc, and ignores index - very different from
#  doing it by index value with [::-1]. Also, you can't store the sorted value
#  in a new variable, only in the original variable. Can't assign to new while
#  doing the .sort() command

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

sorted_list = sorted(sale_prices, reverse=True) #numerical value

print(sorted_list) #sorted() allows you to have sorted variable to use
print(sale_prices) #and doesn't change the original list

sorted_list = sorted(sale_prices, reverse=True) #inverse numerical value

print(sorted_list)
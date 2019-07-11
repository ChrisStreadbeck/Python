# num_list = [1,2,3,4,5,6]
# total = sum(num_list)
# length = len(num_list)
# mean = total / length
# print(mean)

#---------------------------------------
def average(num_list):
  mean = sum(num_list) / len(num_list)
  print(mean)


average([1,2,3,4,5,6,7,8,9])

#---------------------------------------------
# from functools import reduce

# def average(num_list):
#   mean = (reduce(lambda a,b : a+b,num_list)) / len(num_list)
#   print(mean)

# average([1,2,3,4,5,6])

#----------------------------------------------
# from functools import reduce
# import operator

# def average(num_list):
#  mean = (reduce(operator.add,num_list)) / len(num_list)
#  print(mean)

# average([1,2,3,4,5,6])
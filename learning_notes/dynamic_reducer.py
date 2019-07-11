
import operator
from functools import reduce

def dynamic_reducer(collection, op):
    
    operators = {
        "string1": operator.add,
        "string2": operator.sub,
        "string3": operator.mul,
        "string4": operator.truediv
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)

print(dynamic_reducer([1, 2, 3], 'string1'))
print(dynamic_reducer([1, 2, 3], 'string2'))
print(dynamic_reducer([1, 2, 3], 'string3'))
print(dynamic_reducer([1, 2, 3], 'string4'))


# My implementation of map for lists. (list() need not be called on the result)

def my_map(my_lambda, array):
  result = []
  for el in array:
    result.append(my_lambda(el))

  return result

# print(my_map(lambda x: x**2, [1, 2, 3, 4, 5]))

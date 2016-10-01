# For a input array A, return a new array B wherein each number in B is the 
# product of all numbers in A whose index is not that of the corresponding index 
# in A. Runs in O(n) time

def productify(array):
  result = list(map(lambda el: 1, array))
  downward_list = list(map(lambda el: 1, array))

  for i in range(1, len(array)):
    if i < 2:
      result[i] = array[0]
    else:
      result[i] = result[i - 1] * array[i - 1]

  for j in range(len(array) - 2, -1, -1):
    if j == len(array) - 2:
      downward_list[j] = array[j + 1]
    else:
      downward_list[j] = downward_list[j + 1] * array[j + 1]

  for k in range(0, len(array)):
    result[k] = result[k] * downward_list[k]

  return result

# print(productify([2, 3, 4, 5, 6]))

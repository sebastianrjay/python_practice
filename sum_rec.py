# Recursively (and inefficiently) calculate the sum of an integer array in O(n ^ 2) time

def sum_rec(int_list):
  if(len(int_list) == 0):
    return 0
  elif(len(int_list) == 1):
    return int_list[0]

  return int_list[0] + sum_rec(int_list[1:])

# print(sum_rec([1, 2, 3, 4, 5, 6]))

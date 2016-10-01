# O(log(n)) binary search algorithm implementation for sorted arrays

def binary_search(sorted_array, val):
  if(not sorted_array):
    return None

  idx = int(len(sorted_array) / 2)

  if val < sorted_array[idx]:
    return binary_search(sorted_array[:idx], val)
  elif val == sorted_array[idx]:
    return idx
  else:
    return binary_search(sorted_array[idx + 1:], val)

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3))

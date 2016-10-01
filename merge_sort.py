# Python implementation of the classic merge sort array sorting algorithm. Runs 
# in O(n * log(n)) time

def merge(left_array, right_array):
  merged_array, i, j = [], 0, 0

  while i < len(left_array) and j < len(right_array):
    if left_array[i] < right_array[j]:
      merged_array.append(left_array[i])
      i += 1
    else:
      merged_array.append(right_array[j])
      j += 1

  return (merged_array + left_array[i:] + right_array[j:])

def merge_sort(array):
  if(len(array) < 2):
    return array

  mid = int(len(array) / 2)
  left_array, right_array = array[:mid], array[mid:]
  sorted_left, sorted_right = merge_sort(left_array), merge_sort(right_array)

  return merge(sorted_left, sorted_right)

# print(merge_sort([1, 5, 8, 4, 3, 2, 6, 3, 0, 1]))

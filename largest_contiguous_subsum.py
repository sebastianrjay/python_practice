# Return the largest sum of consecutive numbers in an array, when the array 
# contains at least one non-negative number

def largest_contiguous_subsum(int_array):
  best_sum, current_sum = 0, 0

  for num in int_array:
    current_sum += num
    if(current_sum > best_sum):
      best_sum = current_sum
    elif(current_sum < 0):
      current_sum = 0

  return best_sum

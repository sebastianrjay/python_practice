# Return an array of all pairs of numbers in nums_array that sum to k, in O(n)
# time

def pair_sum(nums_array, k):
  nums = set(nums_array)
  pairs = {}

  for num in nums_array:
    if(k - num in nums):
      pair = min([num, k - num]), max([num, k - num])
      pairs[pair] = True

  return list(map(lambda pair: list(pair), pairs.keys()))

# print(pair_sum([3, 4, 67, 8, 5, 4, 3, 24, 0], 8))

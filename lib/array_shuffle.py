# Return a shuffled copy of an array in O(n) time

def shuffle(array):
  shuffled_array = array[:]

  for idx in range(len(array) - 1):
    rand_idx = random.randrange(0, len(array))
    shuffled_array[idx], shuffled_array[rand_idx] = shuffled_array[rand_idx], shuffled_array[idx]

  return shuffled_array

# print(shuffle([1, 2, 3, 4, 5, 6]))

# Longest palindromic substring of a string, calculated in O(n) time and O(n) 
# space complexities. Worst case time complexity (for a string consisting of the 
# same repeating character) is O(n ** 2)

# More details here:
# https://github.com/sebastianrjay/Algorithms/blob/master/longest_palindromic_substring.rb

def update_palindrome_store(string, pals, i, best_len):
  new_pals, deleted_pal_lengths = {}, []

  for (length, indices) in pals.items():
    if length > best_len:
      best_len = length

    if i == indices[1] + 1 and string[i] == string[i - length - 1] and i - length - 1 >= 0:
      new_pals[length + 2] = [indices[0] - 1, indices[1] + 1]
    elif i > indices[1] + 1 and length < best_len:
      deleted_pal_lengths.append(length)

  for length in deleted_pal_lengths:
    del pals[length]

  pals.update(new_pals)

  return best_len

def longest_palindromic_substring(string):
  best_len, i, longest_pal, pals = 0, 1, "", {}

  while i < len(string):
    best_len = update_palindrome_store(string, pals, i, best_len)

    if string[i] == string[i - 1]:
      pals[2] = [i - 1, i]
    elif i - 2 >= 0 and string[i] == string[i - 2]:
      pals[3] = pals[2] = [i - 2, i]

    i += 1

  if best_len > 0:
    left, right = pals[best_len]
  else:
    left, right = 0, 0

  return string[left : right + 1]

# print(longest_palindromic_substring(''))

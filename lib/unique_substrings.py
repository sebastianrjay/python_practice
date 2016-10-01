# Build a list of the unique substrings of a string in O(n ** 2) time

def unique_subs(string):
  subs_hash = {}
  for i in range(0, len(string)):
    for j in range(i + 1, len(string) + 1):
      subs_hash[string[i:j]] = True

  return list(subs_hash.keys())

# print(unique_subs('abc'))

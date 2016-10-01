# Find the intersection of two lists, in O(m + n) time and space complexity

from collections import defaultdict

def fast_list_intersection(list1, list2):
  seen, final_list = defaultdict(lambda: 0), []

  for el in list1:
    seen[el] += 1

  for el in list2:
    if seen[el] > 0:
      seen[el] -= 1
      final_list.append(el)

  return final_list

# print(fast_list_intersection([1, 2, 3, 4, 5, 6, 6], [0, 2, 4, 5.5, 6, 6, 9]))

# Return a list of the subsets shared by two lists. Runs in 
# O(((m + n) ** 2) * (2 ** (m + n))) time

from fast_list_intersection import fast_list_intersection
from array_subsets import array_subsets

def common_subsets(list1, list2):
  intersection = fast_list_intersection(list1, list2)

  return array_subsets(intersection)

print(common_subsets([1, 2, 3, 4, 5, 6, 6], [0, 2, 4, 5.5, 6, 6, 9]))

# Return all subsets of an array. Runs in O((n ** 2) * (2 ** n)) time, if I'm 
# not mistaken

def array_subsets(array):
  sets = [[]]

  for el in array:
    new_sets = list(map(lambda set: set + [el], sets))
    sets.extend(new_sets)

  return sets

# Recursively build an array of the first n numbers of the Fibonacci sequence,
# in O(n ^ 2) time

def fibonacci_numbers(n):
  if(n < 2):
    return [0, 1][:(n + 1)]
  else:
    previous_fibs = fibs(n - 1)
    return previous_fibs + [sum(previous_fibs)]

# print(fibonacci_numbers(8))

# Calculate the sum of all individual digits in a number

def digital_sum(num):
  sum = 0
  for digit in list(str(num)):
    sum += int(digit)
  return sum

# print(digital_sum(123))

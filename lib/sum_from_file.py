# Read in numbers from each line of a file, and calculate their sum

def sum_from_file(filename):
  file, total = open(filename, "r"), 0
  for line in file.readlines():
    num_string = line.strip()
    if(num_string == "#"):
      continue
    else:
      total += int(num_string)

  return total

# print(sum_from_file("nums.txt"))

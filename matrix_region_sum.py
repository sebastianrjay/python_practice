# Find the sum of all numbers within a sub-matrix of a matrix, bounded by the 
# top left and bottom right coordinate pairs. Runs in O(h * w) time, where h and 
# w are the height and width, respectively, of the sub-matrix

def matrix_region_sum(matrix, top_left_coords, bottom_right_coords):
  sum = 0

  for i in range(top_left_coords[0], bottom_right_coords[0] + 1):
    for j in range(top_left_coords[1], bottom_right_coords[1] + 1):
      sum += matrix[i][j]

  return sum

# matrix = [[3, 3, 4, 5, 6], [1, 6, 3, 2, 5], [9, 6, 5, 9, 7], [8, 5, 0, 3, 0], [5, 5, 7, 3, 8]]
# print(matrix_region_sum(matrix, (1, 2), (3, 3)))

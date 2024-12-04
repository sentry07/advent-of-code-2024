example = [
    'MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX',
]

# -------------------------- Part 1 ----------------------------------

# This actually will word search any word in any grid at any position with a defined delta(x,y)
def searchVector(grid, search, rowPos, colPos, rowDelta, colDelta):
  word = ''
  for x in range(len(search)):
    try:
      # necessary to prevent underflow boundary wrapping
      if rowPos + (rowDelta * x) < 0 or colPos + (colDelta * x) < 0:
        return 0
      
      # grab the next letter
      word += grid[rowPos + (rowDelta * x)][colPos + (colDelta * x)]
      
      # check if the word so far matches what we expect
      if word != search[:x+1]:
        return 0
    except:
      # This should trigger when we overflow boundaries
      return 0
  print('Found at {},{} vector {},{}'.format(rowPos,colPos,rowDelta,colDelta))
  return 1

def part1(data):
  grid = []
  found = 0
  
  # Split the lines up into individual characters
  for line in data:
    chars = list(line)
    grid.append(chars)

  # Go through each character in each row and start a search from there in all 8 directions
  # Error handling in the searchVector function will take care of invalid position/vector combinations
  for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
      found += searchVector(grid, 'XMAS', row, col, -1, -1)
      found += searchVector(grid, 'XMAS', row, col, -1, 0)
      found += searchVector(grid, 'XMAS', row, col, -1, 1)
      found += searchVector(grid, 'XMAS', row, col, 0, -1)
      found += searchVector(grid, 'XMAS', row, col, 0, 1)
      found += searchVector(grid, 'XMAS', row, col, 1, -1)
      found += searchVector(grid, 'XMAS', row, col, 1, 0)
      found += searchVector(grid, 'XMAS', row, col, 1, 1)
  return found

# -------------------------- Part 2 ----------------------------------

# This function grabs the two 3 letter words in an X at the position in the grid and checks for MAS forwards or backwards
def searchX(grid, rowPos, colPos):
  if grid[rowPos][colPos] != 'A':
    return 0
  
  word1 = grid[rowPos-1][colPos-1] + 'A' + grid[rowPos+1][colPos+1]
  word2 = grid[rowPos+1][colPos-1] + 'A' + grid[rowPos-1][colPos+1]
  if (word1 == 'MAS' or word1[::-1] == 'MAS') and (word2 == 'MAS' or word2[::-1] == 'MAS'):
    print('Found at {},{}'.format(rowPos,colPos))
    return 1
  return 0


def part2(data):
  grid = []
  found = 0
  for line in data:
    chars = list(line)
    grid.append(chars)

  # Range is cut down by 1 on each end because we look for 'A's first and go from there out
  for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[row]) - 1):
      found += searchX(grid, row, col)
  return found

print(part1(example))
print(part2(example))

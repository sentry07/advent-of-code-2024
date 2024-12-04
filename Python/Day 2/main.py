example = open('example.txt').read().splitlines()

def part1_testReport(values):
  deltas = [a-b for a,b in zip(values[:-1], values[1:])]
  mv = 0
  for delta in deltas:
    if abs(delta) < 1 or abs(delta) > 3:
      return False
    if (delta > 0 and mv == -1):
      return False
    if (delta < 0 and mv == 1):
      return False
    if (delta < 0 and mv == 0):
      mv = -1
    if (delta > 0 and mv == 0):
      mv = 1
  return True
      
  

def part1(data):
  numSafe = 0
  for report in data:
    values = [int(x) for x in report.split()]
    if part1_testReport(values):
      numSafe += 1
  return numSafe

print(part1(example))

def part2_testDampner(values):
  for x in range(len(values)):
    storedVal = list(values)
    storedVal.pop(x)
    if part1_testReport(storedVal):
      return True
  return False
    

def part2(data):
  numSafe = 0
  for report in data:
    values = [int(x) for x in report.split()]
    if part1_testReport(values):
      numSafe += 1
    elif part2_testDampner(values):
      numSafe += 1
  return numSafe

print(part2(example))

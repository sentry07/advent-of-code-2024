example = open('example.txt').read().splitlines()

def part1(data):
  distance = 0
  left = [int(line.split()[0]) for line in data]
  right = [int(line.split()[1]) for line in data]
  left.sort()
  right.sort()
  for l,r in zip(left,right):
    distance += abs(l-r)
  return distance

print(part1(example))


def part2(data):
  similarity = 0
  left = [int(line.split()[0]) for line in data]
  right = [int(line.split()[1]) for line in data]
  for item in left:
    similarity += item * (right.count(item))
  return similarity


print(part2(example))

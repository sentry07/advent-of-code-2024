import re

def part1(data):
  sum = 0
  # Regex really is magical, isn't it?
  matches = re.finditer("mul\(([0-9]*),([0-9]*)\)", data)
  for match in matches:
    a,b = map(int,match.groups())
    sum += a*b
  return sum

print(part1("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"))

def part2(data):
  # Remove everything from the string between the "don't()" and "do()" sections
  newData = re.split(r"don't\(\).*?(?:do\(\)|$)", data)
  # Then reuse Part1's function
  return part1(''.join(newData))

print(part2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"))

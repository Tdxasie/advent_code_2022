with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()

tot = 0
for line in lines:
    digits = [a for a in line if a.isdigit()]
    tot += int(digits[0] + digits[-1])

# challenge 1
print(tot)
# challenge 2

with open('input.txt', 'r') as infile:
    lines = infile.read().splitlines()

first_col = []
second_col = []
for line in lines:
    a, b = line.split('   ')
    a, b = int(a), int(b)
    first_col.append(a)
    second_col.append(b)
    
first_col = sorted(first_col)
second_col = sorted(second_col)

tot = 0
for a, b in zip(first_col, second_col):
    tot += abs(b-a)
    
print(tot)
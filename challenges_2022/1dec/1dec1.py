
# Challenge 1
print(max([sum(list(map(int, i.split(' ')))) for i in [' '.join(open('input.txt').read().splitlines()).split('  ')][0]]))
# Challenge 2
print(sum(sorted([sum(list(map(int, i.split(' ')))) for i in [' '.join(open('input.txt').read().splitlines()).split('  ')][0]])[-3:]))


    
# with open('input.txt', 'r') as infile:
#     lines = infile.read().splitlines()
# tots = []
# tot = 0
# for line in lines:
#     if line == '':
#         tots.append(tot)
#         tot = 0
#         continue
#     tot += int(line)
# # challenge 1
# print(max(tots))
# # challenge 2
# print(sum(sorted(tots)[-3:]))
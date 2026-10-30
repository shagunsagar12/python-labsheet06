from itertools import combinations

s = {1, 2, 3}
elements = list(s)
power_set = []

for r in range(len(elements) + 1):
    for item in combinations(elements, r):
        power_set.append(set(item))

print("Power Set:")
for item in power_set:
    print(item)
numbers = [1, 2, 3, 2, 4, 3, 5]

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate Elements:", sorted(duplicates))
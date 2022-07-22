numbers = [4, 1, 11, 10, 2, 8, 6]
numbers.sort()

total = 0
count = 0
print(numbers)
for i in range(1, len(numbers) - 1):
    total += numbers[i]
    count += 1

print(total // count)
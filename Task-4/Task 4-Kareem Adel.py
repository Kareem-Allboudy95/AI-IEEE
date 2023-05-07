numbers = [10, 20, 30, 40, 50, 50, 60, 70]
# Mode
mode = max(set(numbers), key=numbers.count)
# Mean
mean = sum(numbers) / len(numbers)
# Median
numbers_sorted = sorted(numbers)
middle_index = len(numbers_sorted) // 2
if len(numbers_sorted) % 2 == 0:
    median = (numbers_sorted[middle_index - 1] + numbers_sorted[middle_index]) / 2
else:
    median = numbers_sorted[middle_index]

print("Mode: ", mode)
print("Mean: ", mean)
print("Median: ", median)

##########################################################################################
# another solution Take user input for the numbers

numbers = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    number = int(input("Enter a number: "))
    numbers.append(number)

# Mode
mode = max(set(numbers), key=numbers.count)
# Mean
mean = sum(numbers) / len(numbers)
# Median
numbers_sorted = sorted(numbers)
middle_index = len(numbers_sorted) // 2
if len(numbers_sorted) % 2 == 0:
    median = (numbers_sorted[middle_index - 1] + numbers_sorted[middle_index]) / 2
else:
    median = numbers_sorted[middle_index]

print("Mode: ", mode)
print("Mean: ", mean)
print("Median: ", median)



##########################################################################################
# another solution with libraries

import numpy as np

numbers = [10, 20, 30, 40, 50, 50, 60, 70]
# Mode
mode = np.mode(numbers)
# Mean
mean = np.mean(numbers)
# Median
median = np.median(numbers)

print("Mode: ", mode)
print("Mean: ", mean)
print("Median: ", median)
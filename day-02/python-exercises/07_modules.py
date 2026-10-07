# Python Modules

import statistics
import math

marks = [72, 85, 91, 64, 78]

average = statistics.mean(marks)
highest = max(marks)
lowest = min(marks)

print("Marks:", marks)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Square Root of Average:", round(math.sqrt(average), 2))
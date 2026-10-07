# Modules and Packages

import random
from collections import Counter

marks = [72, 85, 72, 91, 64, 85, 72]

# Module: random
selected_mark = random.choice(marks)

print("Randomly Selected Mark:", selected_mark)

# Package: collections
mark_count = Counter(marks)

print("\nMark Frequency:")
print(mark_count)
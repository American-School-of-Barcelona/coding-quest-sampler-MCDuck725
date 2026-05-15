"""
CodingQuest Problem 18: Inventory check

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

Each line has three parts separated by spaces:
  - A unique item ID
  - A quantity (number)
  - A category name

Write your solution below the comment line.
"""

# --- Load the data (don't change this) ---
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

# Take a look at the first few lines
print(f"Loaded {len(data)} lines.")
print("First 5 lines:")
for line in data[:5]:
    print("  ", line)
print()

# --- Your code here ---



from collections import defaultdict

totals = defaultdict(int)

for line in data:
    parts = line.split()
    quantity = int(parts[1])
    category = parts[2]
    totals[category] += quantity

print("Category totals:")
for cat, total in totals.items():
    print(f" {cat}: {total} (mod 100 = {total % 100})")

print = 1
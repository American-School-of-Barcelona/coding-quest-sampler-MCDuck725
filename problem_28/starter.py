"""
CodingQuest Problem 28: Purchase tickets

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

Write your solution below the comment line.
"""


with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]


print(f"Loaded {len(data)} lines.")
print("First 5 lines:")
for line in data[:5]:
    print("  ", line)
print()


data = """SolarSkies: Rebate 9997
CelestialFlyer: Discount 2886
RyanSpace: Luggage 3500
NovaWings: Tax 156
MartianSpacelines: Fee 1641
OrionAir: Fee 7859
QantasSpace: Discount 2150
StarCruiser: Rebate 2339
NebulaAir: Tax 4507
QantasSpace: Rebate 2671"""

costs = {}

for line in data.strip().split('\n'):
    company, details = line.split(': ')
    item_type, amount = details.split()
    amount = int(amount)
    
    
    if item_type.lower() in ['seat', 'meals', 'luggage', 'fee', 'tax']:
        costs[company] = costs.get(company, 0) + amount
    else:
        costs[company] = costs.get(company, 0) - amount


cheapest_cost = min(costs.values())

print(f"The final cost of the cheapest option is: {cheapest_cost}")

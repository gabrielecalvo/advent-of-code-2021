# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

from utils import get_input

# + [markdown] jp-MarkdownHeadingCollapsed=true tags=[]
# # Day 1
# -

content = get_input("day01.txt")

# ## part 1

# +
values = [int(i) for i in content.split("\n")]

previous_value = 999
increases = 0
for value in values:
    if value > previous_value:
        increases += 1
    previous_value = value

print(f"Solution is: {increases}")
# -

# ## part 2

# +
values = [int(i) for i in content.split("\n")]
triplet_sum = [sum(values[i:i+3]) for i,_ in enumerate(values)][:-2]

previous_value = 999
increases = 0
for value in triplet_sum:
    if value > previous_value:
        increases += 1
    previous_value = value

print(f"Solution is: {increases}")

# + [markdown] jp-MarkdownHeadingCollapsed=true tags=[]
# # Day 2
# -

content = get_input("day02.txt")

# ## part 1

# + tags=[]
x = y = 0

def parse_row(row):
    command, units_str = row.split(" ")
    units = int(units_str)
    if command == "forward":
        return units, 0
    elif command == "down":
        return 0, units
    elif command == "up":
        return 0, -units
    raise ValueError(f"{command}")

for row in content.split("\n"):
    if not row: continue
    dx, dy = parse_row(row) 
    x += dx
    y += dy
    
print(f"Solution {x*y}")
# -

# ## part 2

# +
x = y = aim = 0

def parse_row(row, current_aim):
    """returns horizontal, depth and aim"""
    command, units_str = row.split(" ")
    units = int(units_str)
    if command == "forward":
        return units, current_aim*units, 0
    elif command == "down":
        return 0, 0, units
    elif command == "up":
        return 0, 0, -units
    raise ValueError(f"{command}")

for row in content.split("\n"):
    if not row: continue
    dx, dy, daimd = parse_row(row, aim) 
    x += dx
    y += dy
    aim += daimd
    
print(f"Solution {x*y}")
# -

# # Day 3

content = get_input("day03.txt")
diagnostics = [i for i in content.split("\n") if i]

# ## part 1

# +
from collections import defaultdict, Counter

counts_by_position = defaultdict(lambda: {"0": 0, "1":0}) 

for row in diagnostics:
    for pos, char in enumerate(row):
        counts_by_position[pos][char] +=1 
# -

gamma_rate = ""
epsilon_rate = ""
for pos, counts in counts_by_position.items():
    most_common = max(counts, key=counts.get)
    least_common = min(counts, key=counts.get)
    gamma_rate += most_common
    epsilon_rate += least_common

product = int(gamma_rate,2) * int(epsilon_rate,2)
print(f"Solution {product}")


# ## part 2

def split_by_common_bit(diagnostics, bit_pos):
    stacks = {"0": [], "1": []}
    for d in diagnostics:
        stacks[d[bit_pos]].append(d)
    
    if len(stacks["0"]) > len(stacks["1"]):
        oxigen_candidates = stacks["0"]
        co2_candidate = stacks["1"]
    else:
        oxigen_candidates = stacks["1"]
        co2_candidate = stacks["0"]
    
    return oxigen_candidates, co2_candidate


# +
n = len(diagnostics[0])
oxigen_value = co2_value = None

oxigen_values = diagnostics
for i in range(n):
    oxigen_values = split_by_common_bit(oxigen_values, i)[0]
    if len(oxigen_values) == 1:
        oxigen_value = oxigen_values[0]
        break
        
co2_values = diagnostics
for i in range(n):
    co2_values = split_by_common_bit(co2_values, i)[1]
    if len(co2_values) == 1:
        co2_value = co2_values[0]
        break
# -

product = int(oxigen_value,2) * int(co2_value,2)
print(f"Solution {product}")



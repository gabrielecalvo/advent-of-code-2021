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

# + [markdown] jp-MarkdownHeadingCollapsed=true tags=[] jp-MarkdownHeadingCollapsed=true jp-MarkdownHeadingCollapsed=true tags=[]
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

# + [markdown] jp-MarkdownHeadingCollapsed=true tags=[] jp-MarkdownHeadingCollapsed=true jp-MarkdownHeadingCollapsed=true tags=[]
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

# + [markdown] tags=[] jp-MarkdownHeadingCollapsed=true jp-MarkdownHeadingCollapsed=true tags=[]
# # Day 3
# -

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

# + [markdown] tags=[]
# # Day 4
# -

content = get_input("day04.txt")
content_rows = content.split("\n")

# +
from itertools import product

rowcol = [(r,c) for r,c in product(range(5), range(5))]
        
class Board:
    def __init__(self, rows, name):
        self.name = name
        self.values = [[int(i) for i in r.split()] for r in rows]
        self.mask = [[0 for i in range(5)] for j in range(5)]
        
    def __repr__(self):
        res = ""
        for row, col in rowcol:
            value = self.values[row][col]
            mask = self.mask[row][col]
            prefix = "\n" if col == 0 else ""
            res += f"{prefix}" + (f"({value:>2})" if mask else f" {value:>2} ")
        return res
    
    def tick_number(self, n):
        for row, col in rowcol:
            if self.values[row][col] == n:
                self.mask[row][col] = 1
                return True
        return False
    
    def check_board(self):
        for r in self.mask:
            if sum(r) == 5:
                return True
            
        for c in range(5):
            if sum(r[c] for r in self.mask) == 5:
                return True
            
        return None
        
    def sum_unmasked(self):
        unmarked_sum = 0
        for row, col in rowcol:
            if self.mask[row][col] == 0:
                unmarked_sum += self.values[row][col]
            
        return unmarked_sum
    
def build_boards(content_rows):
    boards = {}
    for i in range(2, len(content_rows), 6):
        boards[i] = Board(content_rows[i:i+5], name=i)
    return boards


# -

# ## part 1

def find_solution(extracted_numbers, boards):
    for n in extracted_numbers:
        for board in boards.values():
            if board.tick_number(n):
                if board.check_board():
                    return board.sum_unmasked() * n


extracted_numbers = [int(i) for i in content_rows[0].split(",")]
boards = build_boards(content_rows)

find_solution(extracted_numbers, boards)


# ## part 2

# +
def find_solution(extracted_numbers, boards):
    remaining_boards = boards.copy()
    for n in extracted_numbers:
        for board_name, board in boards.items():
            if board_name not in remaining_boards: continue
            if not board.tick_number(n): continue
            if not board.check_board(): continue
            remaining_boards.pop(board_name)
            if len(remaining_boards) == 0:
                return board.sum_unmasked() * n

find_solution(extracted_numbers, boards)
# -



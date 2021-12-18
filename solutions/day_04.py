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

# ### part 2

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

# + [markdown] tags=[]
# ## Day 4
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
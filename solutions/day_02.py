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
# ## Day 2
# -

content = get_input("day02.txt")

# ### part 1

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

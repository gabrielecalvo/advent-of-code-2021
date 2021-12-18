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


# +
def process_input(data):
    return [int(i) for i in data.split(",")]

test_content = process_input(get_input("day06_test.txt"))
content = process_input(get_input("day06.txt"))


# + [markdown] jp-MarkdownHeadingCollapsed=true tags=[] jp-MarkdownHeadingCollapsed=true jp-MarkdownHeadingCollapsed=true tags=[]
# ## Day 6
# -

def test_population(pool, days, expected):
    actual = pool.simulate_growth(n_days=days)
    assert actual == expected, f"{actual} == {expected}"


# + [markdown] tags=[]
# ## part 1

# +
from dataclasses import dataclass

@dataclass
class Fish:
    timer: int
    cycle_length: int = 7
    cycle_length_increase: int = 3
    
@dataclass
class FishPool:
    fishes: list[Fish]
    days: int = 0
    
    def __init__(self, starting_timers: list[int], verbose: bool = False):
        self.fishes = [Fish(i) for i in starting_timers]
        self.verbose = verbose
    
    def age(self):
        new_generation = []
        for fish in self.fishes:
            if fish.timer == 0:
                fish.timer = fish.cycle_length
                child_fish = Fish(timer=fish.cycle_length + fish.cycle_length_increase - 2)
                new_generation.append(child_fish)
            fish.timer -= 1
        self.fishes.extend(new_generation)
        self.days += 1
        
        if self.verbose:
            print(f"After {self.days:>2} day: {[f.timer for f in self.fishes]}")
        
    def simulate_growth(self, n_days: int):
        for i in range(n_days):
            self.age()
        return len(self.fishes)


# -

test_population(FishPool(test_content), days=18, expected=26)
test_population(FishPool(test_content), days=80, expected=5934)

# %%time
test_population(FishPool(content), days=80, expected=373378)

# ## part 2

# +
from collections import Counter
import pdb

class FastFishPool:
    days: int = 0
    
    def __init__(self, timers: list[int], verbose: int = 0):
        self.timers_counts = Counter(timers)  # mapping of {timer: number_of_fish}
        self.verbose = verbose
    
    def age(self):
        n_spawning = self.timers_counts.get(0, 0)
        if n_spawning:
            del self.timers_counts[0]
            self.timers_counts[7] = self.timers_counts.get(7, 0) + n_spawning
        self.timers_counts = {k-1: v for k, v in self.timers_counts.items()}
        self.timers_counts[8] = n_spawning
        self.days += 1
        
        if self.verbose > 1: 
            print(f"After {self.days:>2} day: {sorted([i for k,v in self.timers_counts.items() for i in [k]*v])}")

    def simulate_growth(self, n_days: int):
        for i in range(n_days):
            if self.verbose == 1: print(i)
            self.age()
        return sum(self.timers_counts.values())


# -

test_population(FastFishPool(test_content, verbose=0), days=18, expected=26)
test_population(FastFishPool(test_content), days=80, expected=5934)

# %%time
test_population(FastFishPool(content), days=80, expected=373378)

# + tags=[]
# %%time
pool = FastFishPool(content, verbose=0)
test_population(pool, days=256, expected=1682576647495)
# -



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
# ## Day 5
# -

content = get_input("day05.txt")

# +
from collections import defaultdict
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
    @classmethod
    def parse(cls, xy):
        x, y = [int(i) for i in xy.split(",")]
        self = cls(x=x, y=y)
        return self
    
    @property
    def location_id(self) -> tuple[int, int]:
        return self.x, self.y
    
@dataclass
class Pair:
    start: Point
    end: Point
    
    @classmethod
    def parse(cls, row):
        xy1, xy2 = row.split(" -> ")
        self = cls(start=Point.parse(xy1), end=Point.parse(xy2))
        return self
    
    def all_cross_points(self, include_diagonal: bool) -> list[Point]:
        points = []
        if self.start.x == self.end.x:
            x = self.start.x
            step = 1 if self.start.y < self.end.y else -1
            for y in range(self.start.y, self.end.y+step, step):
                points.append(Point(x=x, y=y))
        elif self.start.y == self.end.y:
            y = self.start.y
            step = 1 if self.start.x < self.end.x else -1
            for x in range(self.start.x, self.end.x+step, step):
                points.append(Point(x=x, y=y))
        elif include_diagonal:
            x_step = 1 if self.start.x < self.end.x else -1
            y_step = 1 if self.start.y < self.end.y else -1
            x_rng = range(self.start.x, self.end.x+x_step, x_step)
            y_rng = range(self.start.y, self.end.y+y_step, y_step)
            for x, y in zip(x_rng, y_rng):
                points.append(Point(x=x, y=y))

        return points
        
def calculate_matrix(pairs: list[Pair], include_diagonal=False) -> dict[tuple, int]:
    matrix = defaultdict(int)
    for pair in pairs:
        for point in pair.all_cross_points(include_diagonal=include_diagonal):
            matrix[point.location_id] += 1
    return matrix


# -

# ## part 1

pairs = [Pair.parse(row) for row in content.split("\n") if row]
matrix = calculate_matrix(pairs)
part_1_solution = sum([1 for v in matrix.values() if v>=2])
assert part_1_solution == 5197, f"{part_1_solution}"

# ## part 2

matrix = calculate_matrix(pairs, include_diagonal=True)
part_1_solution = sum([1 for v in matrix.values() if v>=2])
assert part_1_solution == 18605, f"{part_1_solution}"



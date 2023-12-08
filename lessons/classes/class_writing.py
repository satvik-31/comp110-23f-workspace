"""Class Writing for Quiz 3."""

from __future__ import annotations

class ChristmasTreeFarm:
    """A christmas tree farm."""

    plots: list[int]
    # Values represent the size of each tree

# plots - total no of plots in the farm, initial planning - no of plots that will have trees already planted.
    def __init__(self, plots: int, initial_planning: int):
        """Constructor Function."""
        self.plots = []
        i: int = 0
        while i < initial_planning:
            self.plots.append(1)
        i += 1
        while i < plots:
            self.plots.append(0)
    
    # Plot index - Plot Index at which tree should be planted.
    def plant(self, plot_idx: int):
       """Plants a tree at the given plot number."""
       self.plots[plot_idx] = 1

    def growth(self):
        """Increase the size of each tree."""
        for elem in self.plots:
            if elem != 0:
                elem += 1

    def harvest(self,replant: bool) -> int:
        """Replant trees or not."""
        total: int = 0
        i: int = 0 
        while i < len(self.plots):
            if self.plots[i] >= 5:
                total += 1
                if replant is True:
                    self.plots[i] = 1
                else:
                    self.plots[i] = 0
            i += 1
        return total
    
    def __add__(self, element: ChristmasTreeFarm) -> ChristmasTreeFarm:
        """Adds two Christmas Tree Farms."""
        i: int = 0
        total: int = 0
        while i < len(self.plots):
            if self.plots[i] > 0:
                total += 1
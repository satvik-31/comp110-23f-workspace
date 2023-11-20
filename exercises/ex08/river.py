"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730517765"


class River:
    """River class with attributes."""
    day: int 
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears: int): 
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
            
    def check_ages(self):
        """Checks ages of fish and bears."""
        new_list_bear: list[Bear] = []
        new_list_fish: list[Fish] = []
        for bears in self.bears:
            if bears.age <= 5:
                new_list_bear.append(bears)
        self.bears = new_list_bear
        for fish in self.fish:
            if fish.age <= 3:
                new_list_fish.append(fish)
        self.fish = new_list_fish
        return None

    def bears_eating(self):
        """Tracks fish eateen by bears."""
        for bears in self.bears:
            if len(self.fish) >= 5:
                fish_eaten = 3
                self.remove_fish(fish_eaten)
                bears.eat(fish_eaten)
        return None
    
    def check_hunger(self):
        """Tracks bears hunger level."""
        bears_left: list[Bear] = []
        for bears in self.bears:
            if bears.hunger_score >= 0:
                bears_left.append(bears)
        self.bears = bears_left
        return None
        
    def repopulate_fish(self):
        """Birth of new fish."""
        n: int = len(self.fish)
        add: int = (n // 2) * 4
        for fish in range(0, add):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Birth of new bears."""
        n: int = len(self.bears)
        add: int = n // 2
        for bears in range(0, add):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """River view."""
        x: str = self.day
        y: str = self.fish
        z: str = self.bears 
        print(f"~~~ Day {x}: ~~~")
        print(f"Fish population: {len(y)}")
        print(f"Bear population: {len(z)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one river day 7 times."""
        while self.day < 7:
            self.one_river_day()
        return None
    
    def remove_fish(self, amount: int):
        """Removes amount of fish in the river."""
        for fishes in range(min(amount, len(self.fish))):
            if self.fish:
                self.fish.pop(0)
        return None
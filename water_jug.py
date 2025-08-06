from typing import List, Tuple, Any
from state import State

class WaterJugState(State):
    def __init__(self, small: int, large: int) -> None:
        self.small = small  # 3-liter jug
        self.large = large  # 5-liter jug

    def is_goal(self) -> bool:
        return self.large == 4  # goal state is to have 4 liters in the large jug
    
    def __repr__(self) -> str:
        return f"({self.small}, {self.large})"
    
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, WaterJugState):    # check if the other object is an instance of WaterJugState
            return False
        return self.small == other.small and self.large == other.large  # check if the small and large jugs are equal
    
    def __hash__(self) -> int:
        return hash((self.small, self.large))   # hash function to allow the state to be used in sets and dictionaries
    
    def successors(self) -> List[Tuple["WaterJugState", int]]:
        # generate all possible successor states, this function returns a list of tuples
        # each tuple contains a new state and the amount of water moved as a step cost
        
        successors = []
        
        # Fill the small jug
        if self.small < 3:      # if the small jug is not full
            successors.append((WaterJugState(3, self.large), 3 - self.small))   # then fill the small jug
        
        # Fill the large jug
        if self.large < 5:      # if the large jug is not full
            successors.append((WaterJugState(self.small, 5), 5 - self.large))   # then fill the large jug
        
        # Empty the small jug
        if self.small > 0:     # if the small jug is not empty
            successors.append((WaterJugState(0, self.large), self.small))       # then empty the small jug
        
        # Empty the large jug
        if self.large > 0:      # if the large jug is not empty
            successors.append((WaterJugState(self.small, 0), self.large))       # then empty the large jug
        
        # Pour from small to large
        pour_to_large = min(self.small, 5 - self.large)     # amount of water that can be poured from small to large jug
        if pour_to_large > 0:   # if the large jug can take more water
            successors.append((WaterJugState(self.small - pour_to_large, self.large + pour_to_large), pour_to_large))   # then pour from small to large jug
        
        # Pour from large to small
        pour_to_small = min(self.large, 3 - self.small)     # amount of water that can be poured from large to small jug
        if pour_to_small > 0:   # if the small jug can take more water
            successors.append((WaterJugState(self.small + pour_to_small, self.large - pour_to_small), pour_to_small))   # then pour from large to small jug
        
        return successors
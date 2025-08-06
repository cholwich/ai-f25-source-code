from state import State
from typing import List, Tuple

class Node:
    def __init__(self, state: "State", parent: "Node", path_cost: int, depth: int) -> None:
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.depth = depth

    def __lt__(self, other: "Node") -> bool:
        return self.path_cost < other.path_cost
    
def find_state(state: State, frontier: List[Tuple[int, Node]]) -> Tuple[int, Node]:
    for i, (_, node) in enumerate(frontier):
        if node.state == state:
            return i, node
    return -1, None
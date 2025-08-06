from typing import List, Tuple, Any

# Define an abstract base class for State
class State:
    def __init__(self):
        pass
    def is_goal(self) -> bool:
        """
        Check if the current state is a goal state.
        This method should be overridden in subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    def successors(self) -> List[Tuple["State", int]]:
        """
        Generate the successors of the current state.
        This method should be overridden in subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    def __repr__(self) -> str:
        return "State"
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, State):
            return False
        return True
    def __hash__(self) -> int:
        return hash(self.__repr__())
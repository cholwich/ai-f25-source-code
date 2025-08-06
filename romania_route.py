from typing import List, Tuple, Any
from state import State

class RomaniaRouteState:
    def __init__(self, city: str) -> None:
        self.city = city  # current city
        self.routes = {
            "Arad": [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)],
            "Bucharest": [("Pitesti", 101), ("Fagaras", 211), ("Giurgiu", 90), ("Urziceni", 85)],
            "Craiova": [("Drobeta", 120), ("Pitesti", 138), ("Rimnicu Vilcea", 146)],
            "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
            "Eforie": [("Hirsova", 86)],
            "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
            "Giurgiu": [("Bucharest", 90)],
            "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
            "Iasi": [("Neamt", 87), ("Vaslui", 92)],
            "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
            "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
            "Neamt": [("Iasi", 87)],
            "Oradea": [("Sibiu", 151), ("Zerind", 71)],
            "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
            "Rimnicu Vilcea": [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 146)],
            "Sibiu": [("Fagaras", 99), ("Rimnicu Vilcea", 80), ("Arad", 140), ("Oradea", 151)],
            "Timisoara": [("Lugoj", 111), ("Arad", 118)],
            "Urziceni": [("Bucharest", 85), ("Hirsova", 98)],
            "Zerind": [("Oradea", 71), ("Arad", 75)]
        }

    def is_goal(self) -> bool:
        return self.city == "Bucharest"  # goal state is to reach Bucharest
    
    def __repr__(self) -> str:
        return f"{self.city}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, RomaniaRouteState):
            return False
        return self.city == other.city
    
    def __hash__(self) -> int:
        return hash(self.city)
    
    def successors(self) -> List[Tuple["RomaniaRouteState", int]]:
        successors = []
        for city, distance in self.routes[self.city]:
            successors.append((RomaniaRouteState(city), distance))
        return successors
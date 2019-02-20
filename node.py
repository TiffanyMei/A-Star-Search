from abc import ABC, abstractmethod

# DO NOT MODIFY THIS FILE

class Node(ABC):
    """Abstract class that represents a Node of the A* algorithm.

    Parameters
    ----------
    parent : Node
        The parent node.

    g : int or float
        The cost to reach this node from the start node : g(n).


    Attributes
    ----------
    parent : Node
        The parent node.

    g : int or float
        The cost to reach this node from the start node : g(n).

    f : int or float
        The total estimated cost of the cheapest path from start node to the goal through this node: f(n) = g(n) + h(n).

    state : tuple
        The hashable representation of the search state of this node.

    """
    def __init__(self, parent, g):
        self.parent = parent
        self.g = g
        self.f = self.evaluate_heuristic() + self.g
        self.state = self._get_state()

    @abstractmethod
    def generate_children(self):
        """Expands this node by generating successor nodes.

        Returns
        -------
            children : list of Nodes
                The list of child nodes.
        """
        pass

    @abstractmethod
    def is_goal(self):
        """Decides whether this search state is the goal state.

        Returns
        -------
            is_goal : bool
                True if this search state is the goal state, False otherwise.
        """
        pass

    @abstractmethod
    def evaluate_heuristic(self):
        """Evaluates the heuristic function h(n) for this search state,
        i.e. the estimated cost of the cheapest path from this node to the goal.

        Returns
        -------
            h : int or float
                The heuristic estimated cost from this node to the goal.
        """
        pass

    @abstractmethod
    def _get_state(self):
        """Returns an hashable representation of this search state.

        Returns
        -------
            state: tuple
                The hashable representation of the search state
        """
        pass

    def get_path(self):
        """Returns the path from the start node to this node.

        Returns
        -------
            path : list of Nodes
                The path from the start node to this node.
        """
        path = []
        p = self
        while p:
            path.append(p)
            p = p.parent

        return list(reversed(path))

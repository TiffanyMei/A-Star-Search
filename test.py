"""A set of example unit tests.
NOTE: Do not rely on these tests as they are just simple examples.
Your code will be tested on some secret instances of the problems!
"""

import unittest
from problems import FifteensNode, SuperqueensNode
from search import Astar


class TestFifteens(unittest.TestCase):
    def test_constucting_instances(self):
        """Test that an instance of FifteensNode can be created without an error.
        """
        input_str = '1  2  3  4\n5  6  7  8\n9 10  0 11\n13 14 15 12'
        fifteens_root = FifteensNode(input_str=input_str)
        self.assertEqual(str(fifteens_root), '  1  2  3  4\n  5  6  7  8\n  9 10    11\n 13 14 15 12\n')

    def test_goal_states(self):
        """Test that is_goal returns True when the state is the goal configuration.
        """
        final_str = "1  2  3  4\n5  6  7  8\n9 10 11 12\n13 14 15  0"
        fifteens_node = FifteensNode(input_str=final_str)
        self.assertTrue(fifteens_node.is_goal())

    def test_node_expansions(self):
        """Test that generate_children returns 4 children when the empty cell is in the middle region.
        """
        input_str = '1  2  3  4\n5  6  7  8\n9 10  0 11\n13 14 15 12'
        fifteens_root = FifteensNode(input_str=input_str)
        children = fifteens_root.generate_children()
        self.assertTrue(len(children) == 4)

    def test_heuristic_functions(self):
        """Test that evaluate_heuristic returns 0 when the state is the goal state.
        """
        final_str = "1  2  3  4\n5  6  7  8\n9 10 11 12\n13 14 15  0"
        fifteens_node = FifteensNode(input_str=final_str)
        self.assertEqual(fifteens_node.evaluate_heuristic(), 0)

    def test_a_star_algorithm(self):
        """Test that the length of the solution to a sample initial configuration is correct,
        and the last state is the goal.
        """
        input_str = '1  2  3  4\n5  6  7  8\n9 10  0 11\n13 14 15 12'
        fifteens_root = FifteensNode(input_str=input_str)
        fifteens_path = Astar(fifteens_root)
        self.assertEqual(len(fifteens_path), 3)
        self.assertTrue(fifteens_path[-1].is_goal())


class TestSuperqueens(unittest.TestCase):
    def test_constucting_instances(self):
        """Test that an instance of SuperqueensNode can be created without an error."""
        superqueens_root = SuperqueensNode(n=7)
        for i, a in enumerate(str(superqueens_root)):
            if i % 22 == 21:
                self.assertEqual(a, '\n')
            elif (i - i // 22) % 3 == 1:
                self.assertEqual(a, '.')
            else:
                self.assertEqual(a, ' ')

    def test_goal_states(self):
        """Test that is_goal returns True when the state is a goal configuration.
        """
        queen_positions = [(0, 0), (1, 3), (2, 4), (3, 6), (4, 1), (5, 2), (6, 5)]
        superqueens_node = SuperqueensNode(n=7)
        superqueens_node.queen_positions = queen_positions
        self.assertTrue(superqueens_node.is_goal())

    def test_node_expansions(self):
        """Test that generate_children returns without raising an error.
        """
        superqueens_root = SuperqueensNode(n=7)
        superqueens_root.generate_children()

    def test_heuristic_functions(self):
        """Test that evaluate_heuristic returns without raising an error.
        """
        superqueens_root = SuperqueensNode(n=7)
        superqueens_root.evaluate_heuristic()

    def test_a_star_algorithm(self):
        """Test that the length of the solution path is 8 when the board size is 7,
        the last state is the goal state, and there is no queen in the initial state."""
        superqueens_root = SuperqueensNode(n=7)
        superqueens_path = Astar(superqueens_root)
        self.assertEqual(len(superqueens_path), 8)
        self.assertEqual(len(superqueens_path[0].queen_positions), 0)
        self.assertTrue(superqueens_path[-1].is_goal())


if __name__ == '__main__':
    unittest.main()

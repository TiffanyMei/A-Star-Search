from node import Node
import copy

class FifteensNode(Node):
    """Extends the Node class to solve the 15 puzzle.

    Parameters
    ----------
    parent : Node, optional
        The parent node. It is optional only if the input_str is provided. Default is None.

    g : int or float, optional
        The cost to reach this node from the start node : g(n).
        In this puzzle it is the number of moves to reach this node from the initial configuration.
        It is optional only if the input_str is provided. Default is 0.

    board : list of lists
        The two-dimensional list that describes the state. It is a 4x4 array of values 0, ..., 15.
        It is optional only if the input_str is provided. Default is None.

    input_str : str
        The input string to be parsed to create the board.
        The argument 'board' will be ignored, if input_str is provided.
        Example: input_str = '1 2 3 4\n5 6 7 8\n9 10 0 11\n13 14 15 12' # 0 represents the empty cell

    Examples
    ----------
    Initialization with an input string (Only the first/root construction call should be formatted like this):
    #>>> n = FifteensNode(input_str=initial_state_str)
    #>>> print(n)
      5  1  4  8
      7     2 11
      9  3 14 10
      6 13 15 12

    Generating a child node (All the child construction calls should be formatted like this) ::
    #>>> n = FifteensNode(parent=p, g=p.g+c, board=updated_board)
    #>>> print(n)
      5  1  4  8
      7  2    11
      9  3 14 10
      6 13 15 12

    """

    def __init__(self, parent=None, g=0, board=None, input_str=None):
        # NOTE: You shouldn't modify the constructor
        if input_str:
            self.board = []
            for i, line in enumerate(filter(None, input_str.splitlines())):
                self.board.append([int(n) for n in line.split()])
        else:
            self.board = board

        super(FifteensNode, self).__init__(parent, g)

    def generate_children(self):
        """Generates children by trying all 4 possible moves of the empty cell.

        Returns
        -------
            children : list of Nodes
                The list of child nodes.
        """

        # TODO: add your code here
        # You should use self.board to produce children. Don't forget to create a new board for each child
        # e.g you can use copy.deepcopy function from the standard library.
        zero_row = 0
        zero_col = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    zero_row=i
                    zero_col=j
        children = []
        # create new board
        # generate a child
        # put it in list

        # swap w/ left
        if zero_col != 0:
            newboard = copy.deepcopy(self.board)
            newboard[zero_row][zero_col] = newboard[zero_row][zero_col-1]
            newboard[zero_row][zero_col-1] = 0
            childnode1 = FifteensNode(parent=self, g=self.g+1, board=newboard)
            # print(childnode1.__str__())
            children.append(childnode1)

        # swap w/ right
        if zero_col != 3:
            newboard = copy.deepcopy(self.board)
            newboard[zero_row][zero_col] = newboard[zero_row][zero_col+1]
            newboard[zero_row][zero_col+1] = 0
            childnode2 = FifteensNode(parent=self, g=self.g+1, board=newboard)
            # print(childnode2.__str__())
            children.append(childnode2)

        # swap w/ up
        if zero_row != 0:
            newboard = copy.deepcopy(self.board)
            newboard[zero_row][zero_col] = newboard[zero_row-1][zero_col]
            newboard[zero_row-1][zero_col] = 0
            childnode3 = FifteensNode(parent=self, g=self.g+1, board=newboard)
            # print(childnode3.__str__())
            children.append(childnode3)

        # swap w/ down
        if zero_row != 3:
            newboard = copy.deepcopy(self.board)
            newboard[zero_row][zero_col] = newboard[zero_row+1][zero_col]
            newboard[zero_row+1][zero_col] = 0
            childnode4 = FifteensNode(parent=self, g=self.g+1, board=newboard)
            # print(childnode4.__str__())
            children.append(childnode4)

        return children

    def is_goal(self):
        """Decides whether this search state is the final state of the puzzle.

        Returns
        -------
            is_goal : bool
                True if this search state is the goal state, False otherwise.
        """

        # TODO: add your code here
        # You should use self.board to decide.

        bool = True
        bool = bool and (self.board[0][0]==1) and (self.board[0][1]==2) and (self.board[0][2]==3) and (self.board[0][3]==4)
        bool = bool and (self.board[1][0]==5) and (self.board[1][1]==6) and (self.board[1][2]==7) and (self.board[1][3]==8)
        bool = bool and (self.board[2][0]==9) and (self.board[2][1]==10) and (self.board[2][2]==11) and (self.board[2][3]==12)
        bool = bool and (self.board[3][0]==13) and (self.board[3][1]==14) and (self.board[3][2]==15) and (self.board[3][3]==0)
        return bool

    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of moves
        required to reach the goal state from this node.

        Returns
        -------
            h : int or float
                The heuristic value for this state.
        """

        # TODO: add your code here
        # You may want to use self.board here.

        h = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] != 0:
                    row_diff = abs(i - int((self.board[i][j] - 1) / 4))
                    if self.board[i][j] % 4 == 0:
                        col_diff = abs(j-3)
                    else:
                        col_diff = abs(j - (self.board[i][j] % 4 - 1))
                    h = h + row_diff + col_diff
        return h

    def _get_state(self):
        """Returns an hashable representation of this search state.

        Returns
        -------
            state: tuple
                The hashable representation of the search state
        """
        # NOTE: You shouldn't modify this method.
        return tuple([n for row in self.board for n in row])

    def __str__(self):
        """Returns the string representation of this node.

        Returns
        -------
            state_str : str
                The string representation of the node.
        """
        # NOTE: You shouldn't modify this method.
        sb = []  # String builder
        for row in self.board:
            for i in row:
                sb.append(' ')
                if i == 0:
                    sb.append('  ')
                else:
                    if i < 10:
                        sb.append(' ')
                    sb.append(str(i))
            sb.append('\n')
        return ''.join(sb)


class SuperqueensNode(Node):
    """Extends the Node class to solve the Superqueens problem.

    Parameters
    ----------
    parent : Node, optional
        The parent node. Default is None.

    g : int or float, optional
        The cost to reach this node from the start node : g(n).
        In this problem it is the number of pairs of superqueens that can attack each other in this state configuration.
        Default is 1.

    queen_positions : list of pairs
        The list that stores the x and y positions of the queens in this state configuration.
        Example: [(q1_y,q1_x),(q2_y,q2_x)]. Note that the upper left corner is the origin and y increases downward
        Default is the empty list [].
        ------> x
        |
        |
        v
        y

    n : int
        The size of the board (n x n)

    Examples
    ----------
    Initialization with a board size (Only the first/root construction call should be formatted like this):
    # n = SuperqueensNode(n=4)
    # print(n)
         .  .  .  .
         .  .  .  .
         .  .  .  .
         .  .  .  .

    Generating a child node (All the child construction calls should be formatted like this):
    # n = SuperqueensNode(parent=p, g=p.g+c, queen_positions=updated_queen_positions, n=p.n)
    # print(n)
         Q  .  .  .
         .  .  .  .
         .  .  .  .
         .  .  .  .

    """

    def __init__(self, parent=None, g=0, queen_positions=[], n=1):
        # NOTE: You shouldn't modify the constructor
        self.queen_positions = queen_positions
        self.n = n
        super(SuperqueensNode, self).__init__(parent, g)

    def generate_children(self):
        """Generates children by adding a new queen.

        Returns
        -------
            children : list of Nodes
                The list of child nodes.
        """
        # TODO: add your code here
        # You should use self.queen_positions and self.n to produce children.
        # Don't forget to create a new queen_positions list for each child.
        # You can use copy.deepcopy function from the standard library.

        children = []

        # add child column by column
        col = len(self.queen_positions)

        # for every row
        for row in range(self.n):

            # check if this row is empty by comparing with existing queen_positions
            is_empty = True
            for value in self.queen_positions:
                if value[0] == row:
                    is_empty = False
                    break

            # if this row is empty, add a child
            if is_empty:
                # print(row, col)

                # 1) update queens position
                updated_queens_positions = copy.deepcopy(self.queen_positions)
                updated_queens_positions.append((row, col))

                # 2) calculate new g
                updated_g = self.g

                test_row = row
                test_col = col
                while test_row > 0 and test_col > 0:
                    # print("check 1")
                    test_row = test_row-1
                    test_col = test_col-1
                    if (test_row, test_col) in self.queen_positions:
                        updated_g = updated_g + 1

                test_row = row
                test_col = col
                while test_row < self.n and test_col > 0:
                    # print("check 2")
                    test_row = test_row + 1
                    test_col = test_col - 1
                    if (test_row, test_col) in self.queen_positions:
                        updated_g = updated_g + 1

                test_row = row-2
                test_col = col-1
                if (test_row, test_col) in self.queen_positions:
                    updated_g = updated_g + 1
                test_row = row - 1
                test_col = col - 2
                if (test_row, test_col) in self.queen_positions:
                    updated_g = updated_g + 1
                test_row = row + 2
                test_col = col - 1
                if (test_row, test_col) in self.queen_positions:
                    updated_g = updated_g + 1
                test_row = row + 1
                test_col = col - 2
                if (test_row, test_col) in self.queen_positions:
                    updated_g = updated_g + 1

                # 3) generate child
                child = SuperqueensNode(parent=self, g=updated_g, queen_positions=updated_queens_positions, n=self.n)
                children.append(child)

        return children

    def is_goal(self):
        """Decides whether all the queens are placed on the board.

        Returns
        -------
            is_goal : bool
                True if all the queens are placed on the board, False otherwise.
        """
        # You should use self.queen_positions and self.n to decide.

        return len(self.queen_positions) == self.n

    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of conflicts required to reach the final state.

        Returns
        -------
            h : int or float
                The heuristic value for this state.
        """
        # If you want to design a heuristic for this problem, you should use self.queen_positions and self.n.
        # TODO: add your code here (optional)
        return 0

    def _get_state(self):
        """Returns an hashable representation of this search state.

        Returns
        -------
            state: tuple
                The hashable representation of the search state
        """
        # NOTE: You shouldn't modify this method.
        return tuple(self.queen_positions)

    def __str__(self):
        """Returns the string representation of this node.

        Returns
        -------
            state_str : str
                The string representation of the node.
        """
        # NOTE: You shouldn't modify this method.
        sb = [[' . '] * self.n for i in range(self.n)]  # String builder
        for i, j in self.queen_positions:
            sb[i][j] = ' Q '
        return '\n'.join([''.join(row) for row in sb])

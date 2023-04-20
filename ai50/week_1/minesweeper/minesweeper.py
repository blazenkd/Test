'''
AI50 2023
Week 1: minesweeper.py
Complete the implementations of the Sentence class and the MinesweeperAI class in minesweeper.py.
In the Sentence class, complete the implementations of known_mines, known_safes, mark_mine, and mark_safe.
In the MinesweeperAI class, complete the implementations of add_knowledge, make_safe_move, and make_random_move.
'''

import itertools
import random
import copy


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        return self.cells if self.count == len(self.cells) else set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if not self.cells:
            return set()
        elif self.count == 0:
            return self.cells

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1


    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.
        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """

        # Add the given cell to the set of moves made
        self.moves_made.add(cell)

        # Mark the given cell as safe, and update any sequences that contain the cell
        self.mark_safe(cell)

        # Create a new sentence for the AI's knowledge base based on the given cell and count
        cells = set()
        count_cpy = count
        for close_cell in self.return_close_cells(cell):
            if close_cell in self.mines:
                count_cpy -= 1
            if close_cell not in self.mines and close_cell not in self.safes:
                cells.add(close_cell)

        new_sentence = Sentence(cells, count_cpy)

        # Add the new sentence to the knowledge base
        if len(new_sentence.cells) > 0:
            self.knowledge.append(new_sentence)

        # Use the AI's knowledge base to mark any additional cells as safe or as mines
        self.check_knowledge()

        # Use the AI's knowledge base to infer new sentences, and add them to the knowledge base
        self.extra_inference()

    def return_close_cells(self, cell):
        """
        returns cell that are 1 cell away from cell passed in arg
        """
        # returns cells close to arg cell by 1 cell
        close_cells = set()
        for rows in range(self.height):
            for columns in range(self.width):
                if abs(cell[0] - rows) <= 1 and abs(cell[1] - columns) <= 1 and (rows, columns) != cell:
                    close_cells.add((rows, columns))
        return close_cells

    def check_knowledge(self):
        """
        check knowledge for new safes and mines, updates knowledge if possible
        """
        # copies the knowledge to operate on copy
        knowledge_copy = copy.deepcopy(self.knowledge)
        # iterates through sentences

        for sentence in knowledge_copy:
            if len(sentence.cells) == 0:
                try:
                    self.knowledge.remove(sentence)
                except ValueError:
                    pass
            # check for possible mines and safes
            mines = sentence.known_mines()
            safes = sentence.known_safes()

            # update knowledge if mine or safe was found
            if mines:
                for mine in mines:
                    # print(f"Marking {mine} as mine")
                    self.mark_mine(mine)
                    self.check_knowledge()
            if safes:
                for safe in safes:
                    # print(f"Marking {safe} as safe")
                    self.mark_safe(safe)
                    self.check_knowledge()

    def extra_inference(self):
        """
        update knowledge based on inference
        """
        # iterate through pairs of sentences
        for sentence1 in self.knowledge:
            for sentence2 in self.knowledge:
                # check if sentence 1 is subset of sentence 2
                if sentence1.cells.issubset(sentence2.cells):
                    new_cells = sentence2.cells - sentence1.cells
                    new_count = sentence2.count - sentence1.count
                    new_sentence = Sentence(new_cells, new_count)
                    mines = new_sentence.known_mines()
                    safes = new_sentence.known_safes()
                    if mines:
                        for mine in mines:
                            # print(f"Used inference to mark mine: {mine}")
                            # print(f"FinalSen: {new_sentence}")
                            # print(f"Sent1: {sent1copy}")
                            # print(f"Sent2: {sent2copy}")
                            self.mark_mine(mine)

                    if safes:
                        for safe in safes:
                            # print(f"Used inference to mark safe: {safe}")
                            # print(f"FinalSen: {new_sentence}")
                            # print(f"Sent1: {sent1copy}")
                            # print(f"Sent2: {sent2copy}")
                            self.mark_safe(safe)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.
        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        return next((i for i in self.safes - self.moves_made), None)

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """

        # Create a list of all the cells on the board that have not yet been chosen as moves or marked as mines
        available_cells = [(row, col) for row in range(self.height) for col in range(self.width)
                            if (row, col) not in self.moves_made | self.mines]

        # If there are any available cells, return a randomly chosen cell from the list of available cells
        if available_cells:
            return random.sample(available_cells, 1)[0]
        # If there are no available cells left, return None
        else:
            return None

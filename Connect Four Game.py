#
# A Game of Connect Four
#
# Computer Science 111
#
# Zhenglin Wang
#

import random

# Part I Board class
class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """
    def __init__(self, height, width):
        """ a constructor for Board objects
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'

        s += '-' * (self.width * 2 + 1) + '\n'
        for x in range(self.width):
            s += ' ' + str(x % 10)
        s += '\n'
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        for row in range(self.height - 1, -1, -1):
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                break

    def reset(self):
        """ reset the Board object on which it is called by setting all slots 
            to contain a space character
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] != ' ':
                    self.slots[row][col] = ' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column col 
            on the calling Board object. Otherwise, it should return False
        """
        if col >= self.width or col < 0:
            return False
        elif self.slots[0][col] == ' ':
            return True
        else:
            return False
    
    def is_full(self):
        """ returns True if the called Board object is completely full of 
            checkers, and returns False otherwise
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True
    
    def remove_checker(self, col):
        """ Removes the top checker from column col of the called Board object. 
            If the column is empty, then the method should do nothing.
        """
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for col in range(self.width):
            for row in range(self.height - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    
    def is_down_diagonal_win(self, checker):
        """ Checks for a downward diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a upward diagonal win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or 'O', and returns 
            True if there are four consecutive slots containing checker on the 
            board. Otherwise, it should return False
        """
        assert(checker == 'X' or checker == 'O')
        
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False

# Part II Player class
class Player:
    """ a Player class to represent a player of the Connect Four game
    """
    def __init__(self, checker):
        """ constructs a new Player object by initializing the following 
            two attributes
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """ returns a string representing a Player object. The string returned 
            should indicate which checker the Player object is using
        """
        s = 'Player ' + self.checker
        return s
    
    def opponent_checker(self):
        """ returns a one-character string representing the checker of the 
            Player object’s opponent. The method may assume that the calling 
            Player object has a checker attribute that is either 'X' or 'O'
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    
    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns the column 
            where the player wants to make the next move. To do this, the 
            method should ask the user to enter a column number that represents 
            where the user wants to place a checker on the board. The method 
            should repeatedly ask for a column number until a valid column 
            number is given
        """
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if col >= 0 and col < b.width:
                return col
            else:
                print('Try again!')

# Part III helper functions
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

def process_move(p, b):
    """ takes two parameters: a Player object for the player whose move is 
        being processed, and a Board object for the game that is being played
    """
    print(str(p) + "'s turn")
    col = p.next_move(b)
    b.add_checker(p.checker, col)
    print()
    print(b)
    if b.is_win_for(p.checker) == True:
        print(p, 'wins in', p.num_moves, 'moves.')
        print('Congratulations!')
        return True
    elif b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False

class RandomPlayer(Player):
    """ be used for an unintelligent computer player that chooses at random 
        from the available columns
    """
    def next_move(self, b):
        """ choose at random from the columns in the board b that are not yet 
            full, and return the index of that randomly selected column
        """
        self.num_moves += 1
        vals = []
        for col in range(b.width):
            if b.can_add_to(col) == True:
                vals += [col]
        return random.choice(vals)

# Part IV AIPlayer class
class AIPlayer(Player):
    """ a more “intelligent” computer player – one that uses techniques from 
        artificial intelligence (AI) to choose its next move
    """
    def __init__(self, checker, tiebreak, lookahead):
        """ a constructor for AIPlayer objects
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """ returns a string representing an AIPlayer object
        """
        s = 'Player ' + self.checker + ' (' + self.tiebreak + ', ' \
            + str(self.lookahead) + ')'
        return s
    
    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the 
            board, and that returns the index of the column with the maximum 
            score
        """
        new_vals = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                new_vals += [i]
        if self.tiebreak == 'LEFT':
            return min(new_vals)
        elif self.tiebreak == 'RIGHT':
            return max(new_vals)
        else:
            return random.choice(new_vals)
    
    def scores_for(self, b):
        """ Takes a Board object b and determines the called AIPlayer‘s scores 
            for the columns in b. Each column should be assigned one of the 
            four possible scores, based on the called AIPlayer‘s lookahead 
            value. The method should return a list containing one score for 
            each column.
        """
        scores = [50] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, 
                                    self.lookahead - 1)
                opp_scores = opponent.scores_for(b)
                scores[col] = 100 - max(opp_scores)
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """ return the called AIPlayer‘s judgment of its best possible move
        """
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))

# connect_four(Player('X'), Player('O'))
# connect_four(Player('X'), RandomPlayer('O'))
# connect_four(RandomPlayer('X'), RandomPlayer('O'))
# connect_four(Player('X'), AIPlayer('O', 'RANDOM', 5))

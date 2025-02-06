#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below.

class Player:
    '''a data type for a Connect Four player'''
    
    def __init__(self, checker):
        '''constructs a new connect four player'''
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0
        
        
    def __repr__(self):
        '''returns a string representing a Player object'''
        s = 'Player ' + self.checker
        return s
    
    
    def opponent_checker(self):
        '''returns a one-character string representing the checker of the Player object’s opponent'''
        if self.checker == 'X':
            return 'O'
        return 'X'
    
    
    def next_move(self, b):
        '''accepts a Board object b as a parameter and returns the column 
        where the player wants to make the next move.'''
        
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                break
            else:
                print('Try again!')
        return col
                
#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width):
        '''a constructor for board objects'''
        self.height = height
        self.width = width
        self.slots = [[' ']*self.width for row in range(self.height)]
        

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        
        #adds the hyphens
        base = '-'*5
        if self.width == 2:
            s += base + '\n'
        else:
            diff = self.width - 2
            mult = diff * 2
            add = mult*'-'
            s += base + add + '\n'
            
        #adds the numbers beneath
        s += ' '
        for num in range(self.width):
            col_number = str(num % 10)
            s += col_number + ' '
    
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
        
        ### put the rest of the method here ###
            
        if self.slots[-1][col] == ' ':
            self.slots[-1][col] = checker
        else:
            for row in range(self.height):
                if self.slots[row][col] != ' ':
                    break
            self.slots[row - 1][col] = checker

    
    ### add your reset method here ###
    def reset(self):
        '''resets the board to empty'''
        self.slots = [[' ']* self.width for row in range(self.height)] 
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    def can_add_to(self, col):
        '''returns true if col exists and can be added to, false otherwise'''
        if col > (self.width-1) or col < 0:
            return False
        elif self.slots[0][col] != ' ':
            return False
        return True
    
    def is_full(self):
        '''returns true if the board is full, false otherwise'''
        full_cols = 0
        for col in range(self.width):
            if self.can_add_to(col) == False:
                full_cols += 1
        if full_cols == self.width:
            return True
        return False
    
    def remove_checker(self, col):
        '''removes the top checker in col, if col is empty is does nothing'''
        if self.slots[-1][col] != ' ':
            for row in range(self.height):
                if self.slots[row][col] != ' ':
                    break
            self.slots[row][col] = ' '
    
    #is_win helper functions
    #horizontal
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker. """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False
    
    #vertical
    def is_vertical_win(self,checker):
        '''checks for vertical wins for checker'''
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    
    #upwards diagonal
    def is_up_diagonal_win(self,checker):
         '''checks for upwards diagonal win for checker'''
         for row in range(3, self.height):
             for col in range( self.width - 3):
                 if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and \
                    self.slots[row - 3][col + 3] == checker:
                     return True
         return False
     
    def is_down_diagonal_win(self, checker):
        '''checks for upwards diagonal win for checker'''
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False
    
    def is_win_for(self, checker):
        """ put your docstring here """
        assert(checker == 'X' or checker == 'O')
    
        return self.is_down_diagonal_win(checker) or self.is_up_diagonal_win(checker) \
            or self.is_horizontal_win(checker) or self.is_vertical_win(checker)
     
     
            

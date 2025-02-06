#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    '''a data type for an AI Connect Four player'''
    def __init__(self, checker, tiebreak, lookahead):
        '''constructs a new AI connect four player'''
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        '''returns a string representing an AI Player object'''
        s = 'Player ' + self.checker
        s+= " (" + str(self.tiebreak) + ", " + str(self.lookahead) + ")"
        return s
    
    def max_score_column(self, scores):
        '''takes a list scores containing a score for each column of the board, 
        and that returns the index of the column with the maximum score'''
        
        max_score = max(scores)
        cols_max = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                cols_max += [i]
        #tie breakers
        if self.tiebreak == "LEFT":
            return cols_max[0]
        elif self.tiebreak == "RIGHT":
            return cols_max[-1]
        elif self.tiebreak == "RANDOM":
            return random.choice(cols_max)
        
    def scores_for(self, b):
        '''takes a Board object b and determines the called AIPlayer‘s scores for the columns in b'''
        scores = [0] * b.width
        opp = self.opponent_checker()
        for c in range(b.width):
            if b.can_add_to(c) == False:
                scores[c] = -1
            elif b.is_win_for(self.checker) == True:
                scores[c] = 100
            elif b.is_win_for(opp) == True:
                scores[c] = 0
            elif self.lookahead == 0:
                scores[c] = 50
            else:
                b.add_checker(self.checker, c)
                opponent = AIPlayer(opp, self.tiebreak, self.lookahead - 1)
                opponent_scores = opponent.scores_for(b)
                opp_max = max(opponent_scores)
                if opp_max == 0:
                    scores[c] = 100
                elif opp_max == 100:
                    scores[c]= 0
                elif opp_max == 50:
                    scores[c] = 50
                b.remove_checker(c)
        return scores
                
    def next_move(self, b):
        '''return the called AIPlayer‘s judgment of its best possible move'''
        self.num_moves += 1
        scores = self.scores_for(b)
        max_score = self.max_score_column(scores)
        return max_score
        
        
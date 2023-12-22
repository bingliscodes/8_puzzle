#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Benjamin Inglis
# email: binglis@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Kim Baum  
# partner's email: kbaum@bu.edu
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###

    def __init__(self, depth_limit):
        '''constructs a new State object'''
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def add_state(self, new_state):
        '''adds takes a single State object called new_state and adds it to the
           Searcher‘s list of untested states.
        '''
        self.states += [new_state]
        
    def should_add(self, state):
        '''takes a State object called state and returns True if the called Searcher
           should add state to its list of untested states, and False otherwise.
        '''
        if state.creates_cycle() == True:
            return False
        elif self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        else:
            return True

    def add_states(self, new_states):
        '''takes a list State objects called new_states, and that processes the
           elements of new_states one at a time as follows.
        '''

        for state in new_states:
            if self.should_add(state) == True:
                self.add_state(state)


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    def find_solution(self, init_state):
        '''performs a full state-space search that begins at the specified initial
           state init_state and ends when the goal state is found or when the Searcher
           runs out of untested states.
        '''
        self.add_state(init_state)
        
        self.num_tested = 0
        
        while len(self.states) > 0:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None

    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    
### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    ''' Breadth First Searcher
    '''
    def next_state(self):
        '''overrides (i.e., replaces) the next_state method that is inherited
           from Searcher
        '''
        s = self.states[0]
        self.states.remove(s)
        return s

class DFSearcher(Searcher):
    ''' Depth First Searcher
    '''
    def next_state(self):
        s = self.states[-1]
        self.states.remove(s)
        return s
    

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

def h1(state):
    '''takes a State object called state, and that computes and returns
     an estimate of how many additional moves are needed to get from
            state to the goal state.
    '''
    return state.board.num_misplaced()

### Add your other heuristic functions here. ###
def h2(state):
    ''' a heuristic function that assigns a score to a state object based on how
        far away a tile is from its goal position.
        correct positions
    '''
    d = {'0': [0,0],'1': [0,1],'2': [0,2],'3': [1,0],'4': [1,1],\
    '5': [1,2], '6': [2,0], '7': [2,1], '8': [2,2]}
    
    priority = 0
    for row in range(3):
        for col in range(3):
            tile = state.board.tiles[row][col]
            if tile == (3 * row + col):
                priority += 0
            else:
                priority += abs(d[str(tile)][0] - row)
                priority += abs(d[str(tile)][1] - col)
    return priority


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

    def __init__(self, heuristic):
        ''' constructs a new GreedySearcher object
        '''
        Searcher.__init__(self, -1)
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)

    def add_state(self, state):
        ''' overrides (i.e., replaces) the add_state method that is inherited
            from Searcher
        '''
        self.states += [[self.priority(state), state]]

    def next_state(self):
        '''that overrides (i.e., replaces) the next_state method that is
           inherited from Searcher. This version of next_state should choose
           one of the states with the highest priority.
        '''
        s = max(self.states)
        self.states.remove(s)
        return(s[1])
    
        
### Add your AStarSeacher class definition below. ###


class AStarSearcher(GreedySearcher):
    ''' A* Searcher
    '''
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)

    
        

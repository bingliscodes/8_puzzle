#
# eight_puzzle.py (Final project)
#
# driver/test code for state-space search on Eight Puzzles   
#
# name: Benjamin Inglis
# email: binglis@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Kim Baum  
# partner's email: kbaum@bu.edu
#
from searcher import *
from timer import *

def create_searcher(algorithm, param):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * param - a parameter that can be used to specify either
            a depth limit or the name of a heuristic function
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(param)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(param)
    elif algorithm == 'DFS':
        searcher = DFSearcher(param)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(param)
    elif algorithm == 'A*':
        searcher = AStarSearcher(param)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, param):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * param - a parameter that is used to specify either a depth limit
            or the name of a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')
    searcher = create_searcher(algorithm, param)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, param):
    '''Your function should open the file with the specified filename for reading, and 
       should use a loop to process the file one line at a time.
    '''
    file = open(filename, 'r')
    searcher = create_searcher(algorithm, param)
    num_puzzles = 0
    total_moves = 0
    total_states = 0

    for s in file:
        s = str(s[:-1])
        init_board = Board(s)
        init_state = State(init_board, None, 'init')
        soln = None
        try:
            soln = searcher.find_solution(init_state)
            if searcher.find_solution(init_state) == None:
                print(str(s) + ': no solution')
            else:
                string = s + ': ' + str(soln.num_moves) + ' moves, ' + str(searcher.num_tested) + ' states tested'
                print(string)
                num_puzzles += 1
                total_moves += soln.num_moves
                total_states += searcher.num_tested
            
        except KeyboardInterrupt:
            print(str(s) + ': search terminated, no solution', end='\n')
    
    if num_puzzles == 0:
        print()
        print('solved 0 puzzles')
    else:
        print()
        print('solved', num_puzzles, 'puzzles')
        string = 'averages: ' + str(total_moves/num_puzzles) + ' moves, ' \
        + str(total_states/num_puzzles) + ' states tested'
        print(string)
    
    file.close()
        
        

    

    

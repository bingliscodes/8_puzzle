#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Benjamin Inglis
# email: binglis@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for row in range(3):
            for col in range(3):
                self.tiles[row][col] = int(digitstr[3*row + col])
                if int(digitstr[3*row + col]) == 0:
                    self.blank_r = row
                    self.blank_c = col


    ### Add your other method definitions below. ###

    # repr method for Board class
    def __repr__(self):
        """ returns a string representation of a Board object.
        """
        s = ''
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] == 0:
                    s += '_ '
                else:
                    s += str(self.tiles[row][col]) + ' '
            s += '\n'
        return s

    # move_blank method
    def move_blank(self, direction):
        """ takes a direction as input and moves the blank in the Board object.
            If the move is impossible, return False.
        """
        # establish direction is valid 
        if direction == 'up' and self.blank_r > 0 or \
           direction == 'down' and self.blank_r < 2 or \
           direction == 'left' and self.blank_c > 0 or \
           direction == 'right' and self.blank_c < 2:
            # determine new position of blank
            if direction == 'up':
                new_row = self.blank_r - 1
                new_col = self.blank_c
            elif direction == 'down':
                new_row = self.blank_r + 1
                new_col = self.blank_c
            elif direction == 'left':
                new_row = self.blank_r
                new_col = self.blank_c - 1
            elif direction == 'right':
                new_row = self.blank_r
                new_col = self.blank_c + 1

            # take the old tile and move it to the blank, then move the blank
            tile = self.tiles[new_row][new_col]
            self.tiles[self.blank_r][self.blank_c] = tile
            self.tiles[new_row][new_col] = '_'
            # update new blanks
            self.blank_r = new_row
            self.blank_c = new_col
            return True
        # if direction is not valid or out of bounds, return False
        else:
            print('Invalid direction:', direction)
            return False

    # digit_string method
    def digit_string(self):
        """ creates and returns a string of digits corresponding with current board
            contents.
        """
        s = ''
        for row in range(3):
            for col in range(3):
                if str(self.tiles[row][col]) == '_':
                       s += '0'
                else:
                    s += str(self.tiles[row][col])

        return s

    # copy method
    def copy(self):
        """ returns a newly-constructed deep copy of the Board object.
        """
        s = self.digit_string()
        return Board(s)

    #num_misplaced method
    def num_misplaced(self):
        """ counts and returns # of tiles in the Board object that are not in the
            goal state (not including the blank cell)
        """
        
        misplaced_count = 0
        
        # check to see if each tile is in its designated row and column.  If it is
        # not, add 1 to the misplaced counter
        for row in range(3):
            for col in range(3):
                if self.tiles[row][col] != row * 3 + col and \
                   self.tiles[row][col] != 0 and self.tiles[row][col] != '_':
                    misplaced_count += 1
                    #print(self.tiles[row][col])

        return misplaced_count

    # __eq__ method
    def __eq__(self, other):
        """ overwrites == operater.  Returns True if self and other have same tile
            values.
        """
        return self.digit_string() == other.digit_string()
    
        
        
        

            
            
        

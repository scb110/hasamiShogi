# Author: STEPHEN BURKE
# Date: 12/3/2021
# Description: Portfolio Project of the term, I have coded the foundation for two players to enjoy a game of
#                Hasami Shogi (Variant 1).  This is a two player alternating turns styled game with further
#                explanations on game rules and method descriptions included below.

class HasamiShogiGame:
    """This class provides the foundation for two players to engaage in a
    friendly(or not so friendly...) variation 1 game of Hasami Shogi."""

    def __init__(self):
        """ initializer that gives the default board, starts a move counter at 1, creates empty lists to appended to
        based on how many pieces of each color are captured, and initializes the game_state to 'UNFINISHED'       """
        self._board = [[" ", 1, 2, 3, 4, 5, 6, 7, 8, 9], ["a", "R", "R", "R", "R", "R", "R", "R", "R", "R"],
             ["b", ".", ".", ".", ".", ".", ".", ".", ".", "."], ["c", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["d", ".", ".", ".", ".", ".", ".", ".", ".", "."], ["e", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["f", ".", ".", ".", ".", ".", ".", ".", ".", "."], ["g", ".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["h", ".", ".", ".", ".", ".", ".", ".", ".", "."], ["i", "B", "B", "B", "B", "B", "B", "B", "B", "B"]]
        self._count = 1
        self._blacks_captured = []
        self._reds_captured = []
        self._game_state = "UNFINISHED"

    def get_game_state(self):
        """Takes no parameters and returns 'UNFINISHED', 'RED_WON' or 'BLACK_WON' or 'TIE'
        based on lengths of self._blacks_captured and self._reds_captured.  If 7 or less on both, then continue, if exactly 8,
        then return either 'RED_WON' or 'BLACK_WON' based on get_active_player.  If 9, 'TIE'.... """
        if len(self._blacks_captured) <= 7 and len(self._reds_captured) <= 7:
            return "UNFINISHED"
        if len(self._blacks_captured) == 8:
            return "BLACK_WON"
        if len(self._reds_captured) == 8:
            return "RED_WON"
        if len(self._blacks_captured) == 9:
            return "TIE"
        if len(self._reds_captured) == 9:
            return "TIE"

    def print_board(self):
        """Takes no parameters, just prints board in its current state.  No parameters needed,
        no return type needed. This just prints board header then uses for loop to print board."""
        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
        print("*_*_*_*_*_*HASAMI SHOGI VARIANT ONE*_*_*_*_*_*")
        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
        for row in self._board:
            for square in row:
                print(square, end="    ")
            print("\n")

    def get_num_captured_pieces(self, whose_turn):
        """Takes a string parameter that should either be 'RED' or 'BLACK'.
        If whose_turn is RED, then returns length of self._blacks_captured or if BLACK then self._reds_captured"""
        if whose_turn == "RED":
            return len(self._blacks_captured)
        elif whose_turn == "BLACK":
            return len(self._reds_captured)
        else:
            print("User input not identifiable. \nPlease enter either 'RED' or 'BLACK'")

    def get_active_player(self):
        """This method uses a formula from discrete mathematics to alternate whose turn it is every time the count
        variable is incremented.  Thus, after a player's turn finishes, count is incremented and this method
        returns either 'BLACK' if it is now Black's turn or returns 'RED' if it is Red's turn."""
        turn = (-1)**self._count
        if turn == -1:
            return "BLACK"
        if turn == 1:
            return "RED"

    def make_move(self, start_pos, new_pos):
        """
        Ensures valid move, determines capturing status, and can even trigger end result of game.
        Returns True or False based on validity of move
        """
        # check if game is won already...if over, return False
        if self.get_game_state() != "UNFINISHED":
            return False

        # ensure that the coordinates even exist
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
        for letter in start_pos:
            if letter not in nums and letter not in letters:
                return False

        for letter in new_pos:
            if letter not in nums and letter not in letters:
                return False

        if len(start_pos) != 2 or len(new_pos) != 2:
            return False

        # for internal method purposes we are putting coordinates into a list of integers
        # new_list[0] = start_pos row, new_list[1] = start_pos col
        # new_list[2] = new_pos row, new_list[0] = new_pos col,
        moves = [start_pos, new_pos]
        new_list = []
        for move in moves:
            for character in move:
                new_list.append(character)
            for val in range(0, len(new_list)):
                if new_list[val] == 'a':
                    new_list[val] = int(1)
                elif new_list[val] == 'b':
                    new_list[val] = int(2)
                elif new_list[val] == 'c':
                    new_list[val] = int(3)
                elif new_list[val] == 'd':
                    new_list[val] = int(4)
                elif new_list[val] == 'e':
                    new_list[val] = int(5)
                elif new_list[val] == 'f':
                    new_list[val] = int(6)
                elif new_list[val] == 'g':
                    new_list[val] = int(7)
                elif new_list[val] == 'h':
                    new_list[val] = int(8)
                elif new_list[val] == 'i':
                    new_list[val] = int(9)
                else:
                    new_list[val] = int(new_list[val])

        # check if the piece selected to move is of correct color.
        if self.get_square_occupant(start_pos) == "NONE":
            print("You selected a square that has no piece to move!")
            return False
        if self.get_square_occupant(start_pos) != self.get_active_player():
            print("You selected to move an invalid piece.")
            return False

        # check if the destination square is available at all.
        if self.get_square_occupant(new_pos) != "NONE":
            print("Cannot move piece to an occupied square")
            return False

        # verify actual movement occurs
        if new_list[0] == new_list[2] and new_list[1] == new_list[3]:
            print("Passing on a turn is not allowed.\nChoose a destination other than its current square")
            return False

        # verify that move is legal direction
        if new_list[0] != new_list[2] and new_list[1] != new_list[3]:
            print("You can only move a piece up or down a file or left or right on a rank.\nOther movements, such as "
                  "diagonal movements, are not allowed.")
            return False

        # verify path is clear (ie. not 'hopping' pieces)
        if new_list[0] == new_list[2]:
            if new_list[3] > new_list[1]:
                for square in range(new_list[1]+1, new_list[3]):
                    if self._board[new_list[0]][square] != ".":
                        print("Sorry, can't hop over pieces!\nTry a different move!")
                        return False
            else:
                for square in range(new_list[3]+1, new_list[1]):
                    if self._board[new_list[0]][square] != ".":
                        print("Sorry, can't hop over pieces!\nTry a different move!")
                        return False

        if new_list[1] == new_list[3]:
            if new_list[2] > new_list[0]:
                for square in range(new_list[0] + 1, new_list[2]):
                    if self._board[square][new_list[1]] != ".":
                        print("Sorry, can't hop over pieces!\nTry a different move!")
                        return False
            else:
                for square in range(new_list[2] + 1, new_list[0]):
                    if self._board[square][new_list[1]] != ".":
                        print("Sorry, can't hop over pieces!\nTry a different move!")
                        return False
        # make move
        self._board[new_list[0]][new_list[1]] = "."
        if self.get_active_player() == "BLACK":
            self._board[new_list[2]][new_list[3]] = "B"
        if self.get_active_player() == "RED":
            self._board[new_list[2]][new_list[3]] = "R"

        # start a flagging variable for captured piece or not. Initially False unless proven otherwise.

        captured_on_turn = False

        # check corners first
        #
        #    (a,1)                       (a,9)                        (i,1)                          (i,9)
        # (b,1)& (a,2),              (a,8) & (b,9),               (h,1) & (i,2),                 (i,8) and (h,9)

        #       ***   checking for capture of a1  ***

        if new_pos == 'b1':
            if (self.get_square_occupant('a2') == self.get_active_player() and self.get_square_occupant('a1') != "NONE"
                    and self.get_square_occupant('a1') != self.get_active_player()):
                captured_on_turn = True
                if self.get_square_occupant('a1') == "RED":
                    self._reds_captured.append('R')
                    self._board[1][1] = "."
                if self.get_square_occupant('a1') == "BLACK":
                    self._reds_captured.append('B')
                    self._board[1][1] = "."

        if new_pos == 'a2':
            if (self.get_square_occupant('b1') == self.get_active_player() and self.get_square_occupant('a1') != "NONE"
                    and self.get_square_occupant('a1') != self.get_active_player()):
                captured_on_turn = True
                if self.get_square_occupant('a1') == "RED":
                    self._reds_captured.append('R')
                    self._board[1][1] = "."
                if self.get_square_occupant('a1') == "BLACK":
                    self._reds_captured.append('B')
                    self._board[1][1] = "."

        #       ***   checking for capture of a9  ***
        if new_pos == 'b9':
            if (self.get_square_occupant('a8') == self.get_active_player() and self.get_square_occupant('a9') != "NONE"
                    and self.get_square_occupant('a9') != self.get_active_player()):
                captured_on_turn = True
                if self.get_square_occupant('a9') == "RED":
                    self._reds_captured.append('R')
                    self._board[1][9] = "."
                if self.get_square_occupant('a9') == "BLACK":
                    self._reds_captured.append('B')
                    self._board[1][9] = "."

        if new_pos == 'a8':
            if (self.get_square_occupant('b9') == self.get_active_player() and self.get_square_occupant('a9') != "NONE"
                    and self.get_square_occupant('a9') != self.get_active_player()):
                captured_on_turn = True
                if self.get_square_occupant('a9') == "RED":
                    self._reds_captured.append('R')
                    self._board[1][9] = "."
                if self.get_square_occupant('a9') == "BLACK":
                    self._reds_captured.append('B')
                    self._board[1][9] = "."

        #       ***   checking for capture of i1  ***
        if new_pos == 'h1':
            if (self.get_square_occupant('i2') == self.get_active_player() and self.get_square_occupant('i1') != "NONE"
                    and self.get_square_occupant('i1') != self.get_active_player()):
                captured_on_turn = True
                if self.get_square_occupant('i1') == "RED":
                    self._reds_captured.append('R')
                    self._board[9][1] = "."
                if self.get_square_occupant('i1') == "BLACK":
                    self._reds_captured.append('B')
                    self._board[9][1] = "."

        if new_pos == 'i2':
            if (self.get_square_occupant('h1') == self.get_active_player() and self.get_square_occupant('i1') != "NONE"
                    and self.get_square_occupant('i1') != self.get_active_player()):
                captured_on_turn = True
                if self.get_square_occupant('i1') == "RED":
                    self._reds_captured.append('R')
                    self._board[9][1] = "."
                if self.get_square_occupant('i1') == "BLACK":
                    self._reds_captured.append('B')
                    self._board[9][1] = "."

        #       ***   checking for capture of i9  ***
        if new_pos == 'h9':
            if (self.get_square_occupant('i8') == self.get_active_player() and self.get_square_occupant('i9') != "NONE"
                    and self.get_square_occupant('i9') != self.get_active_player()):
                captured_on_turn = True
                if self.get_square_occupant('i9') == "RED":
                    self._reds_captured.append('R')
                    self._board[9][9] = "."
                if self.get_square_occupant('i9') == "BLACK":
                    self._blacks_captured.append('B')
                    self._board[9][9] = "."

        if new_pos == 'i8':
            if (self.get_square_occupant('h9') == self.get_active_player() and self.get_square_occupant('i9') != "NONE"
                    and self.get_square_occupant('i9') != self.get_active_player()):
                captured_on_turn = True
                if self.get_square_occupant('i9') == "RED":
                    self._reds_captured.append('R')
                    self._board[9][9] = "."
                if self.get_square_occupant('i9') == "BLACK":
                    self._blacks_captured.append('B')
                    self._board[9][9] = "."

        # checks row and executes capture only if only contiguous opponents were trapped between two teammates on row
        row_matches = []
        for horizontal_value in range(1, 10):
            color = self._board[new_list[2]][new_list[3]]
            piece = self._board[new_list[2]][horizontal_value]
            if piece == color and horizontal_value != new_list[3]:
                row_matches.append(horizontal_value)

        for match in row_matches:
            consecutive_potential = []

            if match > new_list[3] and (match - new_list[3]) > 1:
                for piece_between_matches in range(new_list[3] + 1, match):
                    consecutive_potential.append(self._board[new_list[2]][piece_between_matches])

                if (self.get_active_player() == "BLACK" and "." not in consecutive_potential
                        and "B" not in consecutive_potential):
                    captured_on_turn = True
                    for piece_between_matches in range(new_list[3] + 1, match):
                        self._board[new_list[2]][piece_between_matches] = '.'
                        self._reds_captured.append("R")

                if (self.get_active_player() == "RED" and "." not in consecutive_potential
                        and "R" not in consecutive_potential):
                    captured_on_turn = True
                    for piece_between_matches in range(new_list[3] + 1, match):
                        self._board[new_list[2]][piece_between_matches] = '.'
                        self._blacks_captured.append("B")

            if match < new_list[3] and (new_list[3] - match) > 1:
                for piece_between_matches in range(match + 1, new_list[3]):
                    consecutive_potential.append(self._board[new_list[2]][piece_between_matches])

                if (self.get_active_player() == "BLACK" and "." not in consecutive_potential
                        and "B" not in consecutive_potential):
                    captured_on_turn = True
                    for piece_between_matches in range(match + 1, new_list[3]):
                        self._board[new_list[2]][piece_between_matches] = '.'
                        self._reds_captured.append("R")

                if (self.get_active_player() == "RED" and "." not in consecutive_potential
                        and "R" not in consecutive_potential):
                    captured_on_turn = True
                    for piece_between_matches in range(match + 1, new_list[3]):
                        self._board[new_list[2]][piece_between_matches] = '.'
                        self._blacks_captured.append("B")

        # checks column and executes capture only if only contiguous opponents were trapped between two teammates on col

        col_matches = []
        for vertical_match in range(1, 10):
            color = self._board[new_list[2]][new_list[3]]
            piece = self._board[vertical_match][new_list[3]]
            if piece == color and vertical_match != new_list[2]:
                col_matches.append(vertical_match)

        for match in col_matches:
            consecutive_potential = []

            if match > new_list[2] and (match - new_list[2]) > 1:
                for piece_between_matches in range(new_list[2] + 1, match):
                    consecutive_potential.append(self._board[piece_between_matches][new_list[3]])

                if (self.get_active_player() == "BLACK" and "." not in consecutive_potential
                        and "B" not in consecutive_potential):
                    captured_on_turn = True
                    for piece_between_matches in range(new_list[2] + 1, match):
                        self._board[piece_between_matches][new_list[3]] = '.'
                        self._reds_captured.append("R")

                if (self.get_active_player() == "RED" and "." not in consecutive_potential
                        and "R" not in consecutive_potential):
                    captured_on_turn = True
                    for piece_between_matches in range(new_list[2] + 1, match):
                        self._board[piece_between_matches][new_list[3]] = '.'
                        self._blacks_captured.append("B")

            if new_list[2] > match and (new_list[2] - match) > 1:
                for piece_between_matches in range(match + 1, new_list[2]):
                    consecutive_potential.append(self._board[piece_between_matches][new_list[3]])

                if (self.get_active_player() == "BLACK" and "." not in consecutive_potential
                        and "B" not in consecutive_potential):
                    captured_on_turn = True
                    for piece_between_matches in range(match + 1, new_list[2]):
                        self._board[piece_between_matches][new_list[3]] = '.'
                        self._reds_captured.append("R")

                if (self.get_active_player() == "RED" and "." not in consecutive_potential
                        and "R" not in consecutive_potential):
                    captured_on_turn = True
                    for piece_between_matches in range(match + 1, new_list[2]):
                        self._board[piece_between_matches][new_list[3]] = '.'
                        self._blacks_captured.append("B")

        # conditional captures summary
        if captured_on_turn is True:
            if self.get_active_player() == "BLACK":
                print(f"Nice capture! Black has captured {len(self._reds_captured)} red piece(s) total now!")

            if self.get_active_player() == "RED":
                print(f"Nice capture! Red has captured {len(self._blacks_captured)} black piece(s) total now!")

            if self.get_game_state()=="RED_WON":
                print("CONGRATULATIONS TO TEAM RED FOR WINNING THE GAME!")
                return False

            if self.get_game_state()=="BLACK_WON":
                print("CONGRATULATIONS TO TEAM RED FOR WINNING THE GAME!")
                return False

            if self.get_game_state()=="TIE":
                print("Oof!  To win requires capturing 8, not 9!  This game was a tie!")
                return False

        if len(self._reds_captured) <= 7 and len(self._blacks_captured) <= 7:
            self._count += 1
            return True

    def get_square_occupant(self, pos):
        """Takes the coordinate parameter. if value on self._board is 'R' returns "RED, if value on self._board is 'B'
        returns "BlACK" and if the square is empty this method simply returns  "NONE" """
        char_list = [pos[0], pos[1]]

        for val in range(0, len(char_list)):
            if char_list[val] == 'a':
                char_list[val] = int(1)
            if char_list[val] == 'b':
                char_list[val] = int(2)
            if char_list[val] == 'c':
                char_list[val] = int(3)
            if char_list[val] == 'd':
                char_list[val] = int(4)
            if char_list[val] == 'e':
                char_list[val] = int(5)
            if char_list[val] == 'f':
                char_list[val] = int(6)
            if char_list[val] == 'g':
                char_list[val] = int(7)
            if char_list[val] == 'h':
                char_list[val] = int(8)
            if char_list[val] == 'i':
                char_list[val] = int(9)
            else:
                char_list[val] = int(char_list[val])
        if self._board[char_list[0]][char_list[1]] == 'B':
            return "BLACK"
        elif self._board[char_list[0]][char_list[1]] == 'R':
            return "RED"
        else:
            return "NONE"

def main():
    "This is for actual game play.  It takes user input on a while loop that lasts until there's a tie or a winner."
    print("----------------------------------------------")
    print("\t\t  WELCOME TO HASAMI SHOGI\n\t\t  -BY STEPHEN BURKE")
    print("----------------------------------------------\n\n")
    print("\t\t\tRULES\n\n1. Movement: Pieces only move vertically and horizontally and cannot hop a piece or "
          "replace a piece. \n(Similiar to the 'rook' in chess, but without capturing by replacement.)\n\n2. Captures: "
          "To capture a piece or pieces you must make a move that sandwiches a piece or contiguous\n "
          "pieces of the opposite color between pieces of your color.  No blank squares are permitted for a capture."
          "\nIf a move procures the scenario that the two adjacent pieces are of the opposite color of the corner piece"
          "\n(disregarding the diagonal piece) then the corner piece can be captured.\n\n"
          "3. Turns:  Black goes first, then Red and alternating it goes until a win or tie occurs.  Enter movements"
          "\n by typing the square of the piece you want to move, followed by enter, then the destination square, "
          "followed by enter.\nEx.'i9' (press enter) 'g9' (press enter)\n\n4. Winning:  To win, a player must capture "
          "exactly eight pieces.  9 results in a tie, and 7 or less means the game is still on.\n\n\n\n")
    play = HasamiShogiGame()
    stop_game = False
    while stop_game is False:
        play.print_board()
        print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*\n")
        print(f"It is {play.get_active_player()}'s turn to move")
        pick_piece = input(f"{play.get_active_player()}, enter a piece to move: ")
        to_square = input(f"Now, {play.get_active_player()}, enter a destination square to move to: ")
        play.make_move(pick_piece, to_square)
        if play.get_game_state()!="UNFINISHED":
            print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
            print("\t\tTHANKS FOR PLAYING HASAMI SHOGI")
            print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
            stop_game = True


if __name__ == '__main__':
    main()

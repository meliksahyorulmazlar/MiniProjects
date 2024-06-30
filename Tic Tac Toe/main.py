#Tic Tac Toe in python
#one is in functional programming
#the other is in object oriented programming
board = [[" "," "," "],[" "," "," "],[" "," "," "]]

game_works = True
count = 0

def print_board():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("___________")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("___________")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

def play_turn(choice:str):
    turn_over = False
    while turn_over != True:
        x = int(input("i Index"))
        y = int(input("j Index"))
        if board[x][y] == " ":
            board[x][y] = choice
            turn_over = True

def check_game():
    #Horizontal check
    for list in board:
        if list.count("X") == 3:
            return (False,"X won")
        elif list.count("Y") == 3:
            return (False,"O won")
    #Vertical
    for i in range(len(board)):
        count_x = 0
        count_o = 0
        for j in range(3):
            if board[i][j] == "X":
                count_x += 1
            elif board[i][j] == "O":
                count_o += 1
        if count_x == 3:
            return (False,"X won")
        elif count_o == 3:
            return (False,"O won")

    #Diagonal (left to right)
    count_x = 0
    count_o = 0
    for i in range(3):
        if board[i][i] == "X":
            count_x += 1
        elif board[i][i] == "O":
            count_o += 1
    if count_x == 3:
        return (False, "X won")
    elif count_o == 3:
        return (False, "O won")
    #Diagonal (right to left)
    count_x = 0
    count_o = 0
    for i in range(2,-1,-1):
        j = 2-i
        if board[i][j] == "X":
            count_x += 1
        elif board[i][j] == "O":
            count_o += 1
    if count_x == 3:
        return (False, "X won")
    elif count_o == 3:
        return (False, "O won")

    #check if the game has finished and there are no empty spaces left
    empty = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                empty += 1
    if empty == 0:
        return False,"Draw"
    else:
        return True,""

"""if __name__ == "__main__":
    while game_works:
        print_board()
        count += 1
        if count % 2 == 0:
            play_turn(choice="X")
            game_works = check_game()[0]
        elif count % 2 == 1:
            play_turn(choice="O")
            game_works = check_game()[0]



    print_board()
    result =check_game()[1]
    print(result)"""


#oop
class TicTacToe:
    def __init__(self):
        self.board = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.game_works = True
        self.count = 0
        self.play()

    def print_board(self):
        print(f" {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} ")
        print("___________")
        print(f" {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} ")
        print("___________")
        print(f" {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} ")

    def play_turn(self,choice: str):
        turn_over = False
        while turn_over != True:
            x = int(input("i Index"))
            y = int(input("j Index"))
            if self.board[x][y] == " ":
                self.board[x][y] = choice
                turn_over = True

    def check_game(self):
        # Horizontal check
        for list in self.board:
            if list.count("X") == 3:
                return (False, "X won")
            elif list.count("Y") == 3:
                return (False, "O won")
        # Vertical
        for i in range(len(self.board)):
            count_x = 0
            count_o = 0
            for j in range(3):
                if self.board[i][j] == "X":
                    count_x += 1
                elif self.board[i][j] == "O":
                    count_o += 1
            if count_x == 3:
                return (False, "X won")
            elif count_o == 3:
                return (False, "O won")

        # Diagonal (left to right)
        count_x = 0
        count_o = 0
        for i in range(3):
            if self.board[i][i] == "X":
                count_x += 1
            elif self.board[i][i] == "O":
                count_o += 1
        if count_x == 3:
            return (False, "X won")
        elif count_o == 3:
            return (False, "O won")
        # Diagonal (right to left)
        count_x = 0
        count_o = 0
        for i in range(2, -1, -1):
            j = 2 - i
            if self.board[i][j] == "X":
                count_x += 1
            elif self.board[i][j] == "O":
                count_o += 1
        if count_x == 3:
            return (False, "X won")
        elif count_o == 3:
            return (False, "O won")

        # check if the game has finished and there are no empty spaces left
        empty = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if board[i][j] == " ":
                    empty += 1
        if empty == 0:
            return False, "Draw"
        else:
            return True, ""

    def play(self):
        while self.game_works:
            self.print_board()
            self.count += 1
            if self.count % 2 == 0:
                self.play_turn(choice="X")
                self.game_works = self.check_game()[0]
            elif self.count % 2 == 1:
                self.play_turn(choice="O")
                self.game_works = self.check_game()[0]

        self.print_board()
        result = self.check_game()[1]
        print(result)


if __name__ == "__main__":
    t = TicTacToe()


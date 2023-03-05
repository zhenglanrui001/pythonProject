import copy
class Sokoban:
    def __init__(self, board):
        self.__board = board
        self.__init_board = copy.deepcopy(board)
        self.__list = []
    def find_player(self):
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if self.__board[i][j] == "P":
                    return i,j
    def is_complete(self):
        count = 0
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                if self.__board[i][j] == "o":
                    count += 1
        if count == 0:
            return True
        else:
            return False
    def steps(self):
        return len(self.__list)
    def restart(self):
        self.__board = self.__init_board
        self.__list = []
    def undo(self):
        if len(self.__list) > 1:
            self.__list.pop()
            self.__board = self.__list[-1]
        else:
            self.__board = self.__init_board
    def move(self, direction):
        position = self.find_player()
        x = position[0]
        y = position[-1]
        if direction == "d":
            if 0 <= y < len(self.__board[x])-2:
                if self.__board[x][y+1] == "o" or self.__board[x][y+1] == "*":
                    pass
                elif self.__board[x][y+1] == "#":
                    if self.__board[x][y+2] == "o":
                        self.__board[x][y] = " "
                        self.__board[x][y+1] = "P"
                        self.__board[x][y+2] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x][y+2] == " ":
                        self.__board[x][y] = " "
                        self.__board[x][y+1] = "P"
                        self.__board[x][y+2] = "#"
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x][y+2] == "*":
                        pass
                elif self.__board[x][y+1] == " ":
                    self.__board[x][y] = " "
                    self.__board[x][y+1] = "P"
                    self.__list.append(copy.deepcopy(self.__board))
            elif y == len(self.__board[x]) - 1:
                if self.__board[x][0] == " ":
                    self.__board[x][0] = "P"
                    self.__board[x][y] = " "
                    self.__list.append(copy.deepcopy(self.__board))
                elif self.__board[x][0] == "#":
                    if self.__board[x][1] == "o":
                        self.__board[x][0] = "P"
                        self.__board[x][1] = " "
                        self.__board[x][-1] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x][1] == "*":
                        pass
                    elif self.__board[x][1] == " ":
                        self.__board[x][1] = "#"
                        self.__board[x][0] = "P"
                        self.__board[x][-1] = " "
                        self.__list.append(copy.deepcopy(self.__board))
            elif y == len(self.__board[x]) - 2:
                if self.__board[x][-1] == "*" or self.__board[x][-1] == "o":
                    pass
                else:
                    if self.__board[x][-1] == " ":
                        self.__board[x][-1] = "P"
                        self.__board[x][-2] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x][-1] == "#":
                        if self.__board[x][0] == " ":
                            self.__board[x][0] = "#"
                            self.__board[x][-1] = "P"
                            self.__board[x][-2] = " "
                            self.__list.append(copy.deepcopy(self.__board))
                        elif self.__board[x][0] == "o":
                            self.__board[x][0] = " "
                            self.__board[x][-1] = "P"
                            self.__board[x][-2] = " "
                            self.__list.append(copy.deepcopy(self.__board))
                        elif self.__board[x][0] == "*" or self.__board[x][0] == "#":
                            pass
        elif direction == "a":
            if 2 <= y < len(self.__board[x]):
                if self.__board[x][y-1] == "o" or self.__board[x][y-1] == "*":
                    pass
                elif self.__board[x][y-1] == "#":
                    if self.__board[x][y-2] == "o":
                        self.__board[x][y] = " "
                        self.__board[x][y-1] = "P"
                        self.__board[x][y-2] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x][y-2] == " ":
                        self.__board[x][y-2] = "#"
                        self.__board[x][y-1] = "P"
                        self.__board[x][y] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x][y-2] == "*":
                        pass
                elif self.__board[x][y-1] == " ":
                    self.__board[x][y] = " "
                    self.__board[x][y-1] = "P"
                    self.__list.append(copy.deepcopy(self.__board))
            elif y == 0:
                if self.__board[x][-1] == " ":
                    self.__board[x][y] = " "
                    self.__board[x][-1] = "P"
                    self.__list.append(copy.deepcopy(self.__board))
                elif self.__board[x][-1] == "#":
                    if self.__board[x][-2] == "o":
                        self.__board[x][-2] = " "
                        self.__board[x][-1] = "P"
                        self.__board[x][0] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x][-2] == "*" or self.__board[x][-2] == "#":
                        pass
                    elif self.__board[x][-2] == " ":
                        self.__board[x][-1] = "P"
                        self.__board[x][-2] = "#"
                        self.__board[x][0] = " "
                        self.__list.append(copy.deepcopy(self.__board))
            elif y == 1:
                if self.__board[x][0] == "o" or self.__board[x][0] == "*":
                    pass
                else:
                    if self.__board[x][0] == " ":
                        self.__board[x][0] = "P"
                        self.__board[x][1] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x][0] == "#":
                        if self.__board[x][-1] == "o":
                            self.__board[x][-1] = " "
                            self.__board[x][0] = "P"
                            self.__board[x][1] = " "
                            self.__list.append(copy.deepcopy(self.__board))
                        elif self.__board[x][-1] == " ":
                            self.__board[x][-1] = "#"
                            self.__board[x][0] = "P"
                            self.__board[x][1] = " "
                            self.__list.append(copy.deepcopy(self.__board))
                        elif self.__board[x][-1] == "*" or self.__board[x][-1] == "#":
                            pass
        elif direction == "w":
            if 2 <= x < len(self.__board):
                if self.__board[x-1][y] == "o" or self.__board[x-1][y] == "*":
                    pass
                elif self.__board[x-1][y] == "#":
                    if self.__board[x-2][y] == "o":
                        self.__board[x][y] = " "
                        self.__board[x-1][y] = "P"
                        self.__board[x-2][y] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x-2][y] == " ":
                        self.__board[x][y] = " "
                        self.__board[x-1][y] = "P"
                        self.__board[x-2][y] = "#"
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x-2][y] == "*":
                        pass
                elif self.__board[x-1][y] == " ":
                    self.__board[x][y] = " "
                    self.__board[x-1][y] = "P"
                    self.__list.append(copy.deepcopy(self.__board))
            elif x == 0:
                if self.__board[-1][y] == " ":
                    self.__board[x][y] = " "
                    self.__board[-1][y] = "P"
                    self.__list.append(copy.deepcopy(self.__board))
                elif self.__board[-1][y] == "#":
                    if self.__board[-2][y] == "o":
                        self.__board[-2][y]= " "
                        self.__board[-1][y] = "P"
                        self.__board[0][y] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[-2][y] == " ":
                        self.__board[-2][y] = "#"
                        self.__board[-1][y] = "P"
                        self.__board[0][y] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[-2][y] == "*" or self.__board[-2][y] == "#":
                        pass
            elif x == 1:
                if self.__board[0][y] == "*" or self.__board[0][y] == "o":
                    pass
                else:
                    if self.__board[0][y] == " ":
                        self.__board[0][y] = "P"
                        self.__board[1][y] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[0][y] == "#":
                        if self.__board[-1][y] == " ":
                            self.__board[-1][y] = "#"
                            self.__board[0][y] = "P"
                            self.__board[1][y] = " "
                            self.__list.append(copy.deepcopy(self.__board))
                        elif self.__board[-1][y] == "o":
                            self.__board[0][y] = "P"
                            self.__board[1][y] = " "
                            self.__board[-1][y] = " "
                            self.__list.append(copy.deepcopy(self.__board))
                        elif self.__board[-1][y] == "*" or self.__board[-1][y] == "#":
                            pass
        elif direction == "s":
            if 0 <= x < len(self.__board)-2:
                if self.__board[x+1][y] == "o" or self.__board[x+1][y] == "*":
                    pass
                elif self.__board[x+1][y] == "#":
                    if self.__board[x+2][y] == "o":
                        self.__board[x][y] = " "
                        self.__board[x+1][y] = "P"
                        self.__board[x+2][y] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x+2][y] == " ":
                        self.__board[x][y] = " "
                        self.__board[x+1][y] = "P"
                        self.__board[x+2][y] = "#"
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[x+2][y] == "*":
                        pass
                elif self.__board[x+1][y] == " ":
                    self.__board[x][y] = " "
                    self.__board[x+1][y] = "P"
                    self.__list.append(copy.deepcopy(self.__board))
            elif x == len(self.__board) - 1:
                if self.__board[0][y] == " ":
                    self.__board[x][y] = " "
                    self.__board[0][y] = "P"
                    self.__list.append(copy.deepcopy(self.__board))
                else:
                    if self.__board[0][y] == "#":
                        if self.__board[1][y] == "o":
                            self.__board[1][y] = " "
                            self.__board[0][y] = "P"
                            self.__board[-1][y] = " "
                            self.__list.append(copy.deepcopy(self.__board))
                        elif self.__board[1][y] == " ":
                            self.__board[1][y] = "#"
                            self.__board[0][y] = "P"
                            self.__board[-1][y] = " "
                            self.__list.append(copy.deepcopy(self.__board))
                        elif self.__board[1][y] == "*" or self.__board[1][y] == "#":
                            pass
            elif x == len(self.__board) - 2:
                if self.__board[-1][y] == " ":
                    self.__board[-1][y] = "P"
                    self.__board[-2][y] = " "
                    self.__list.append(copy.deepcopy(self.__board))
                elif self.__board[-1][y] == "*" or self.__board[-1][y] == "o":
                    pass
                elif self.__board[-1][y] == "#":
                    if self.__board[0][y] == " ":
                        self.__board[0][y] = "#"
                        self.__board[-1][y] = "P"
                        self.__board[-2][y] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[0][y] == "o":
                        self.__board[0][y] = " "
                        self.__board[-1][y] = "P"
                        self.__board[-2][y] = " "
                        self.__list.append(copy.deepcopy(self.__board))
                    elif self.__board[0][y] == "#" or self.__board[0][y] == "*":
                        pass
    def __str__(self):
        string = " ".join(self.__board[0])
        for i in range(1,len(self.__board)):
            word = "\n" + " ".join(self.__board[i])
            string += word
        return string

board = [
    [" "," "," "],
    ["P","#","o"],
    [" "," "," "]
]
game = Sokoban(board)
game.move("d")
print(game.is_complete())
game.restart()
print(game.is_complete())
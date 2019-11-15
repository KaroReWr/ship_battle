import ship_factory

class Board:
    water_board = []


    def __init__(self, beginning, the_end):
        self.beginning = beginning
        self.the_end = the_end

    def new_board(self):
        for row in range(0, self.the_end):
            insideBoard = []
            for column in range(0, self.the_end):
                insideBoard.append(".")
            self.water_board.append(insideBoard)
        return self

    def print_water_board(self):
        for i in range(self.beginning, len(self.water_board)):
            row = ""
            for j in range(self.beginning, len(self.water_board)):
                row += " " + str(self.water_board[i][j]) + " "
            print(row)

    def shoot_return_field(self,x,y):
        return self.water_board[x][y]

    def add_coordinate(self,x,y):
        if self.water_board[x][y] != ".":
            return "Change the coordinate, ship is already there."
        else:
            self.water_board[x][y] = "S"

    def nope(self, x,y):
        self.water_board[x][y] = "P"

    def bingo(self, x, y):
        self.water_board[x][y] = "T"

    def getCordinate(self, x, y):
       return self.water_board[x][y]


if __name__ == '__main__':
    moja = Board(0, 10)
    moja.new_board()
    print(moja.shoot_return_field(0,2))

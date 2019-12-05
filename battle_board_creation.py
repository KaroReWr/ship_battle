class Board:
    def __init__(self, beginning, the_end):
        self.beginning = beginning
        self.the_end = the_end
        self.water_board = []

    def new_board(self):
        for row in range(0, self.the_end):
            inside_board = []
            for column in range(0, self.the_end):
                inside_board.append(".")
            self.water_board.append(inside_board)
        return self

    def print_water_board(self):
        print("  A  B  C  D  E  F  G  H  I  J ")
        for i in range(self.beginning, len(self.water_board)):
            row = str(i)
            for j in range(self.beginning, len(self.water_board)):
                row += " " + str(self.water_board[i][j]) + " "
            print(row)

    def return_flat_board(self):
        flat_board = ""
        for i in range(self.beginning, len(self.water_board)):
            row = str(i)
            for j in range(self.beginning, len(self.water_board)):
                row += " " + str(self.water_board[i][j]) + " "
            flat_board += row
        return flat_board

    def print_shadow_board(self):
        print("  A  B  C  D  E  F  G  H  I  J ")
        for i in range(self.beginning, len(self.water_board)):
            row = str(i)
            for j in range(self.beginning, len(self.water_board)):
                if str(self.water_board[i][j]) == "S":
                    row += " . "
                else:
                    row += " " + str(self.water_board[i][j]) + " "
            print(row)


    def add_coordinate(self, x, y):
        if self.water_board[x][y] != ".":
            return "Change the coordinate, ship is already there."
        else:
            self.water_board[x][y] = "S"

    def shoot_return_field(self, x, y):
        y = letter_to_number(y)
        return self.water_board[x][y]

    def nope(self, x, y):
        self.water_board[x][y] = "P"

    def bingo(self, x, y):
        self.water_board[x][y] = "T"

    def get_coordinate(self, x, y):
        xx = letter_to_number(x)
        return self.water_board[xx][y]

    def get_coordinate_line(self, x, y):
        xx = letter_to_number(x)
        line = str(x) + str(y) + self.get_coordinate(xx, y)
        return line

    def set_coordinate(self, x, y, value):
        xx = letter_to_number(x)
        self.water_board[xx][y] = value


def letter_to_number(coordinate_to_change):
    if coordinate_to_change == "A":
        return 0
    if coordinate_to_change == "B":
        return 1
    if coordinate_to_change == "C":
        return 2
    if coordinate_to_change == "D":
        return 3
    if coordinate_to_change == "E":
        return 4
    if coordinate_to_change == "F":
        return 5
    if coordinate_to_change == "G":
        return 6
    if coordinate_to_change == "H":
        return 7
    if coordinate_to_change == "I":
        return 8
    if coordinate_to_change == "J":
        return 9
    return coordinate_to_change


if __name__ == '__main__':
    board = Board(0, 10)
    board.new_board()
    board.get_coordinate("A", 2)

from ship_factory import Ship
from ship_Battle_Board import Board



karo_board = Board(0,10)


def add_pack_of_the_ships(board,pack):
    for ship in pack:
        for coordinates in ship:
            if board[i][j] == ".":
                board[x][y] = "S"
            else:
                print("Field not empty")

 if __name__ == '__main__':
     print(karo_board.shoot_return_field())
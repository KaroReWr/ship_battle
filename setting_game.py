from ship_factory import Ship
from battle_board_creation import Board

karo_board = Board(0,10)
karo_board.new_board()
armada = [[[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]], [[7, 7], [7, 8], [7, 9]]]

def add_pack_of_the_ships(board,armada):
    for ship in armada:
        for coord in ship:
            x = coord[0]
            y = coord[1]
            board.add_coordinate(x,y)


if __name__ == '__main__':
     print(add_pack_of_the_ships(karo_board,armada))
     karo_board.print_water_board()
from ship_factory import Ship
from battle_board_creation import Board

#from jacek_ship import *

karo_board = Board(0,10)
karo_board.new_board()
armada_karo = [[[0, 0]], [[0, 9]], [[9, 9]], [[7, 8]],[[2, 8], [2, 9]], [[5, 6], [6, 6]], [[4, 4], [5, 4]],[[8, 2], [8, 3], [8, 4]], [[2, 0],[3, 0],[4, 0]], [[6, 0], [7, 0], [8, 0], [9, 0]]]



def add_pack_of_the_ships(board,armada):
    for ship in armada:
        for coord in ship:
            x = coord[0]
            y = coord[1]
            board.add_coordinate(x,y)



if __name__ == '__main__':
    add_pack_of_the_ships(karo_board,armada_karo)
    karo_board.bingo(0,0)
    karo_board.print_shadow_board()
    print(" " * 20)
    print("-" * 30)
    print(" " * 20)
    karo_board.print_water_board()



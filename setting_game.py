from ship_factory import Ship
from battle_board_creation import Board
from jacek_ship import armada_jacek


karo_board = Board(0,10)
karo_board.new_board()
armada_karo = [[[0, 0]], [[0, 9]], [[9, 9]], [[7, 8]],[[2, 8], [2, 9]], [[5, 6], [6, 6]], [[4, 4], [5, 4]],[[8, 2], [8, 3], [8, 4]], [[2, 0],[3, 0],[4, 0]], [[6, 0], [7, 0], [8, 0], [9, 0]]]


def add_pack_of_the_ships(board,armada):
    for ship in armada:
        for coord in ship:
            x = coord[0]
            y = coord[1]
            board.add_coordinate(x,y)

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
    jacek_board = Board(0,10)
    jacek_board.new_board()
    add_pack_of_the_ships(jacek_board,armada_jacek)
    print(jacek_board.get_coordinate("A",1))




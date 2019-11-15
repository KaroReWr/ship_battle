from ship_factory import Ship
from battle_board_creation import Board

karo_board = Board(0,10)
karo_board.new_board()
armada = [[[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]], [[7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [7, 13]]]

def add_pack_of_the_ships(board,armada):
    for ships in armada:
        for ship in ships:
            for coord in ship:
                if board[ships][ship][coord] == ".":
                    board[ships][ship][coord] = "S"
                else:
                    print("Field not empty")
    return board

if __name__ == '__main__':
     print(add_pack_of_the_ships(karo_board,armada)
from battle_board_creation import Board
from jacek_ship import armada_jacek

karo_board = Board(0, 10)
karo_board.new_board()
armada_karo = [[[0, 0]], [[0, 9]], [[9, 9]], [[7, 8]], [[2, 8], [2, 9]], [[5, 6], [6, 6]], [[4, 4], [5, 4]],
               [[8, 2], [8, 3], [8, 4]], [[2, 0], [3, 0], [4, 0]], [[6, 0], [7, 0], [8, 0], [9, 0]]]


def add_pack_of_the_ships(board, armada):
    for ship in armada:
        for coord in ship:
            x = coord[0]
            y = coord[1]
            board.add_coordinate(x, y)


if __name__ == '__main__':
    jacek_board = Board(0, 10)
    jacek_board.new_board()
    add_pack_of_the_ships(jacek_board, armada_jacek)
    # jacek_board.print_water_board()
    add_pack_of_the_ships(karo_board, armada_karo)
    player1_board = karo_board
    player1 = open("player1.txt", "w")
    player1.writelines(karo_board.return_flat_board())
    player1.close()
    player2 = open("player2.txt", "w")
    player2.writelines(jacek_board.return_flat_board())
    player2.close()
    player1 = open("player1.txt", "r")
    board_karo = player1.read()
    print(board_karo)




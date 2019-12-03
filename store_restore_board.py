from battle_board_creation import *


def save_board(board_to_save, filename):
    f = open(filename, "w")
    for x in range(0, board_to_save.the_end):
        for y in range(0, board_to_save.the_end):
            line = board_to_save.get_coordinate_line(x, y)
            f.write(line)
            f.write("\n")
    f.close()


test_board = Board(0, 10)
test_board.new_board()
test_board.set_coordinate('C', 3, "S")
test_board.print_water_board()

save_board(test_board, "board1.txt")

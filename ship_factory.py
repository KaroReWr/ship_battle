from copy import copy

from battle_board_creation import letter_to_number


def get_start_coordinates():
    first_ship_coordinates = []
    coordinates = input("What are coordinates for first ship (format 'LETTERnumber'): ")
    coordinate_x_letter_to_num = letter_to_number(coordinates[0])
    first_ship_coordinates.append(coordinate_x_letter_to_num)
    first_ship_coordinates.append(int(coordinates[1]))
    return first_ship_coordinates


def get_mast_number():
    mast_number = int(input("How many masts do you need for this ship? "))
    return mast_number


def get_ship_position():
    position = input("What should be position for the ship? Vertical or horizontal?\n Select v/h: ")
    return position


def get_ship_with_all_data():
    start_coordinate = get_start_coordinates()
    mast_number = get_mast_number()
    position = get_ship_position()

    if mast_number == 1:
        return [start_coordinate]

    add_x = add_y = 0

    ship_to_return = []
    if position == "v":
        add_y = 1
    else:
        add_x = 0

    for mast in range(mast_number):
        start_coordinate[0] += add_x
        start_coordinate[1] += add_y
        base = copy(start_coordinate)
        ship_to_return.append(base)

    return ship_to_return


def create_armada(item_number):
    armada = []
    for number in range(item_number):
        armada.append(get_ship_with_all_data())
    return armada

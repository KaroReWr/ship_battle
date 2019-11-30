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
    while not 0 < mast_number < 5:
        print("Incorrect number of masts! Select number 1,2,3 or 4")
    return mast_number


def get_ship_position():
    position = input("What should be position for the ship? Vertical or horizontal?\n Select v/h: ")
    while position != "v" or position != "h":
        print("Incorrect position. Please select 'v' or 'h'.")
    return position


def get_all_data_for_ship():
    start_coordinate = get_start_coordinates()
    mast_number = get_mast_number()
    position = get_ship_position()
    return start_coordinate, mast_number, position


def create_ship(start_coordinate=None, mast_number=None, position=None):
    mast_number, position, start_coordinate = get_coordinates_if_none_is_given(mast_number, position, start_coordinate)

    if mast_number == 1:
        return [start_coordinate]

    add_x = add_y = 0

    ship_to_return = []
    if position == "v":
        add_y = 1
    elif position == "h":
        add_x = 1

    for mast in range(mast_number):
        base = copy(start_coordinate)
        base[0] += add_x * mast
        base[1] += add_y * mast
        ship_to_return.append(base)

    return ship_to_return


def get_coordinates_if_none_is_given(mast_number, position, start_coordinate):
    if start_coordinate is None:
        all_data = get_all_data_for_ship()
        start_coordinate = all_data[0]
        mast_number = all_data[1]
        position = all_data[2]
    return mast_number, position, start_coordinate


def create_armada(item_number):
    armada = []
    for number in range(item_number):
        armada.append(create_ship())
    return armada

if __name__ == '__main__':
    print(get_coordinates_if_none_is_given(None, None, None))
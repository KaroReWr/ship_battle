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


def get_ship_with_all_data(self):
    start_coordinate = self.get_start_coordinates()
    mast_number = self.get_mast_number(self)
    position = self.get_ship_position(self)
    ship = [start_coordinate]
    if mast_number == 1:
        return ship
    if position == "v":
        for mast in range(mast_number - 1):
            base = copy(start_coordinate)
            base[1] = base[1] + mast + 1
            ship.append(base)
    if position == "h":
        for mast in range(mast_number - 1):
            base = copy(start_coordinate)
            base[0] = base[0] + mast + 1
            ship.append(base)
    return ship


def create_armada(item_number):
    armada = []
    for number in range(item_number):
        armada.append(get_ship_with_all_data())
    return armada


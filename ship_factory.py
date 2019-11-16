from copy import copy

class Ship:

    def get_start_coordinates(self):
        first_ship_coordinates = []
        coordinates = input("What are coordinates for first ship (format xy): ")
        first_ship_coordinates.append(int(coordinates[0]))
        first_ship_coordinates.append(int(coordinates[1]))
        return first_ship_coordinates

    def get_mast_number(self):
        mast_number = int(input("How many masts do you need for this ship? "))
        return mast_number

    def get_ship_position(self):
        position = input("What should be position for the ship? Vertical or horizontal?\n Select v/h: ")
        return position


    def get_ship_with_all_data(self):
        start_coordinate = Ship.get_start_coordinates(self)
        mast_number = Ship.get_mast_number(self)
        position = Ship.get_ship_position(self)
        ship = [start_coordinate]
        if mast_number == 1:
            return ship
        if position == "v":
            for mast in range(mast_number - 1):
                baze = copy(start_coordinate)
                baze[1] = baze[1] + mast + 1
                ship.append(baze)
        if position == "h":
            for mast in range(mast_number - 1):
                baze = copy(start_coordinate)
                baze[0] = baze[0] + mast + 1
                ship.append(baze)
        return ship


masts = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
def create_armada(item_number):
    armada = []
    for number in range(item_number):
        ship_baze = Ship()
        armada.append(ship_baze.get_ship_with_all_data())
    return armada



if __name__ == '__main__':
    pass
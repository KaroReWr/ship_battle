class Ship:

    def get_start_coordinates(self):
        first_ship_coordinates = []
        coordinates = input("What are coordinates for first ship (format xy): ")
        first_ship_coordinates.append(int(coordinates[0]))
        first_ship_coordinates.append(int(coordinates[1]))
        return first_ship_coordinates

    def get_mast_number(self):
        mast_number = int(input("How many masts do you need for this sheep? "))
        return mast_number

    def get_ship_position(self):
        position = input("What should be position for the ship? Vertical or horizontal?\n Select v/h: ")
        return position


    def get_ship_with_all_data(self):
        start_coordinate = Ship.get_start_coordinates(self)
        mast = Ship.get_mast_number(self)
        position = Ship.get_ship_position(self)
        x = 0
        y = 0
        ship = [start_coordinate]
        for i in range(1, mast):
            next_coord = [0,0]
            if position == "h":
                x = i
                next_coord[0] = start_coordinate[0] + x
                next_coord[1] = start_coordinate[1]
            elif position == "v":
                y = i
                next_coord[0] = start_coordinate[0]
                next_coord[1] = int(start_coordinate[1] + y)

            ship.append(next_coord)
        return ship

masts = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


if __name__ == '__main__':
    a = Ship()
    print(a.get_ship_with_all_data())




import types
from copy import copy


def create_ship_new_way(first_mast_coordinates: list, position: str, mast_number: int):
    ship = [first_mast_coordinates]
    if mast_number == 1:
        return ship
    if position == "v":
        for mast in range(mast_number-1):
            baze = copy(first_mast_coordinates)
            baze[1] = baze[1] + mast + 1
            ship.append(baze)
    if position == "h":
        for mast in range(mast_number-1):
            baze = copy(first_mast_coordinates)
            baze[0] = baze[0] + mast + 1
            ship.append(baze)
    return ship


if __name__ == '__main__':
    print(create_ship_new_way([1,1],"h",3))



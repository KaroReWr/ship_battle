import types
def create_ship_new_way(first_mast_coordinates: list, position: str, mast_number: int):
    ship = first_mast_coordinates
    if mast_number == 1:
        return ship
    if position == "v":
        baze = first_mast_coordinates
        for mast in mast_number:
            baze[1] = baze[1] + 1
            ship.append(baze)
    pass



if __name__ == '__main__':
    ship = [[0, 0]]
    baze = [0, 0]
    for mast in range(1,3):
        baze[1] = baze[1] + mast
        ship.append(baze)
    print(ship)

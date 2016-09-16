import os

from ..model.ship import Ship


class Armada:
    def __init__(self, path):
        self.ships = {}

        file_path = os.path.join(path)
        with open(file_path, 'r') as file_name:
            lines = file_name.readlines()
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                if char in 'BDRCS':
                    ship = self.ships.get(char)
                    if ship:
                        ship.location.append((j, i))
                    else:
                        self.ships[char] = Ship([(j, i)])

    def check_hit(self, point):
        """
        Checks any of the ships in the armada were hit

        :param point: point to check
        :type point: tuple(int, int)
        :rtype: int
        :return: Name of ship was hit and sunk, 1 if a ship was hit, 0 if miss
        """
        for ship in self.ships:
            status = self.ships[ship].check_hit(point)
            if status == 2:
                self.ships.pop(ship)
                return ship
            if status == 1:
                return status
        return 0

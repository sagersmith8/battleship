from ship import Ship
import os


class Armada:
    def __init__(self, path):
        self.ships = {}
        lines = []
        file_path = os.path.join(path)
        with open(file_path, 'r') as file_name:
            lines.append(file_name.readlines())
        for i, line in enumerate(lines[0]):
            for j, char in enumerate(line):
                if char in 'BDRCS':
                    ship = self.ships.get(char)
                    if ship:
                        ship.location.append((i, j))
                    else:
                        self.ships[char] = Ship([(i, j)])

    def check_hit(self, point):
        """
        Checks any of the ships in the armada were hit

        :param point: point to check
        :type point: tuple(int, int)
        :rtype: int
        :return: 2 if a ship was hit and sunk, 1 if a ship was hit, 0 if miss
        """
        for ship in self.ships:
            status = self.ships[ship].check_hit(point)
            if status == 2:
                self.ships.pop(ship)
            if status > 0:
                return status
        return 0

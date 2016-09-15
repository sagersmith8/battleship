
class Ship:
    def __init__(self, location):
        self.location = location

    def check_hit(self, point):
        """
        Checks if a point hits a ship

        :param point: point to check
        :type point: tuple(int, int)
        :rtype: int
        :return: 2 if ship was hit and sunk, 1 if ship was hit, 0 if miss
        """
        if point in self.location:
            self.location.remove(point)
            if len(self.location) == 0:
                return 2
            return 1
        return 0

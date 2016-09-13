import requests

def fire(int x, int y):
    """
    Sends a fire request to the opponent's server
    Gets a response from the server

    :param x: number of column that was selected by user
    :type x: int
    :param y: number of row that was selected by user
    :type y: int
    :return: ?
    """
    payload = {'x': x, 'y': y};
    r = requests.post("localhost:5000", data = payload)

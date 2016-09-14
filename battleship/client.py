import requests
import logging

logger = logging.getLogger(__name__)


def fire(x, y):
    """
    Sends a fire request to the opponent's server
    Gets a response from the server

    :param x: number of column that was selected by user
    :type x: int
    :param y: number of row that was selected by user
    :type y: int
    :rtype: None
    :return: No return, but sends a request
    """
    payload = {
        'x': x,
        'y': y
    }

    r = requests.post('http://localhost:5000/', payload)
    print r.text
    logger.debug("Made Request: {}".format(r))


if __name__ == '__main__':
    pass

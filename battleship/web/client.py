import requests
import logging
import sys

logger = logging.getLogger(__name__)


def fire(ip, port, x, y):
    """
    Sends a fire request to the opponent's server
    Gets a response from the server

    :param ip: ip to send the fire message to
    :type: str
    :param port: port the server is listening on
    :type: str
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

    print 'info', ip, port, payload
    fire_request = requests.post('http://{}:{}/'.format(ip, port), payload)
    info = fire_request.text.rfind('=')
    payload['shot'] = fire_request.text[info+1:]
    update_board_request = requests.post(
        'http://0.0.0.0:5000/update_board', payload
    )
    print fire_request.text
    print update_board_request.text

if __name__ == '__main__':
    fire(*sys.argv[1:])

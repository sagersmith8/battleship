from bottle import route, run
from jinja2 import Environment, FileSystemLoader
from os.path import dirname
import requests


JINJA_ENV = Environment(
    loader=FileSystemLoader(dirname(__file__) + '/templates/'),
    extensions=['jinja2.ext.autoescape'])


@route('/')
def hello():
    """
    Welcomes the player to the game

    :rtype: str
    :return: Html string
    """
    return 'Welcome to battleship'


@route('/own_board.html')
def own_board():
    """
    Displays our board

    :rtype: str
    :return: Html string
    """
    return 'my own board'


@route('/opponent_board.html')
def opponent_board():
    """
    Displays the opponents board

    :rtype: str
    :return: Html string
    """
    return 'their board yo'


def respond(template_file, params):
    """
    Responds with the template file

    :param template_file: template file to respond with
    :type template_file: str
    :param params: dictionary of attributes to pass
    :type params: dict
    :rtype: str
    :return: The file rendered as a string
    """
    tpl = JINJA_ENV.get_template(template_file)
    return tpl.render(**params)

if __name__ == '__main__':
    run(host='localhost', port=5000, debug=True)

@route(/<x>/<y>)
def handle_fire(int x, int y):
    """
    Receives fire request from the opponent and handles it accordingly
        - Sends a response to the opponent

    :param x: number of the column of the incomming attack
    :type x: int
    :param y: number of the row of the incomming attack
    :type y: int
    :return: ?
    """
    pass

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

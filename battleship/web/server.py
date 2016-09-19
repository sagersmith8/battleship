import sys
from os.path import dirname, abspath
import time
from bottle import route, run, request, error, static_file
from jinja2 import Environment, FileSystemLoader
from flask import url_for
from battleship.model.armada import Armada

JINJA_ENV = Environment(
    loader=FileSystemLoader(dirname(dirname(dirname(__file__)))+'/templates/'),
    extensions=['jinja2.ext.autoescape']
)


enemy_board = []
for row in xrange(10):
    enemy_board.append([])
    for col in xrange(10):
        enemy_board[row].append(0)
print enemy_board


@route('/static/<file>')
def serve_file(file):
    file_name = dirname(dirname(dirname(__file__)))+'/static'
    return static_file(file, root=file_name)


@route('/own_board.html')
def own_board():
    """
    Displays our board

    :rtype: str
    :return: Html string
    """
    return respond(
        'own_board.html',
        {
            'armada': armada
        }

    )


@route('/opponent_board.html')
def opponent_board():
    """
    Displays the opponents board

    :rtype: str
    :return: Html string
    """
    return respond(
        'opponent_board.html',
        {
            'board': enemy_board
        }
    )


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


@route('/', method='POST')
def handle_fire():
    """
    Receives fire request from the opponent and handles it accordingly
        - Sends a response to the opponent

    :rtype: str
    :return: "Value is x, y"
    """
    x = request.forms.get('x')
    y = request.forms.get('y')
    point = (int(x), int(y))
    hit = armada.check_hit(point)
    print 'Fired at', point, hit
    return (
        'hit={}'.format(hit)
        if str(hit) not in 'CBRSD'
        else 'hit=1&sink={}'.format(hit)
    )


@route('/update_board', method='POST')
def update_board():
    """
    Receives fire request from the opponent and handles it accordingly
        - Sends a response to the opponent

    :rtype: str
    :return: "Value is x, y"
    """
    x = int(request.forms.get('x'))
    y = int(request.forms.get('y'))
    shot = int(request.forms.get('shot'))
    enemy_board[y][x] = shot
    time.sleep(1)
    return (
        'Updated board'
    )


@error(404)
def handle_404(*args):
    print '404'


@error(410)
def handle_410(*args):
    print '410'


@error(400)
def handle_400():
    print '400'


def print_armada(*args):
    """
    Prints the armada location

    :rtype: None
    :return: No return but prints ship locations
    """
    for ship in armada.ships:
        print (
            'Ship {}'.format(ship),
            'Location: {}'.format(armada.ships[ship].location)
        )

if __name__ == '__main__':
    port = sys.argv[1]
    armada = Armada(sys.argv[2])
    print_armada()
    run(host='localhost', port=int(port), debug=True)

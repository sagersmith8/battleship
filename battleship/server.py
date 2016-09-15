from jinja2 import Environment, FileSystemLoader
from os.path import dirname
from bottle import route, run, request, error
import sys
from armada import Armada

JINJA_ENV = Environment(
    loader=FileSystemLoader(dirname(__file__) + '/templates/'),
    extensions=['jinja2.ext.autoescape'])
points_checked = set()


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


@error(404)
def handle_404():
    print '404'


@error(410)
def handle_410():
    print '410'


@error(400)
def handle_400():
    print '400'


def print_armada():
    for ship in armada.ships:
        print (
            'Ship {}'.format(ship),
            'Location: {}'.format(armada.ships[ship].location)
        )

if __name__ == '__main__':
    port = sys.argv[1]
    armada = Armada(sys.argv[2])
    print_armada()
    run(host='localhost', port=5000, debug=True)

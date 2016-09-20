import sys
from os.path import dirname
from bottle import route, run, request, error, static_file, HTTPError
from jinja2 import Environment, FileSystemLoader
from battleship.model.armada import Armada

JINJA_ENV = Environment(
    loader=FileSystemLoader(dirname(dirname(dirname(__file__)))+'/templates/'),
    extensions=['jinja2.ext.autoescape']
)


enemy_board = []
for row in xrange(10):
    enemy_board.append([])
    for col in xrange(10):
        enemy_board[row].append(-1)
print enemy_board

board = []
for row in xrange(10):
    board.append([])
    for col in xrange(10):
        board[row].append(-1)


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
            'board': board,
            'background_image': {
                'C': 'http://www.iboats.com/sites/mastercraft/site_page_19088/images/l_topdownviewofprostarskiboatbymastercraft.png',  # NOQA
                'B': 'http://www.iboats.com/sites/mastercraft/site_page_19088/images/l_topdownviewofmastercraftsx35boatmodel.png',  # NOQA
                'S': 'http://stoneycreekcreative.com/bayarea/wp-content/uploads/2013/10/X30_top_profile.png',  # NOQA
                'D': 'http://www.iboats.com/sites/mastercraft/site_page_19088/images/l_xstartopdownviewshowinglayoutofboat-mastercraft.png',  # NOQA
                'R': 'http://www.onlyinboards.com/getmetafile/4b337fef-c357-4695-825d-130bdfc16df2/2012-Centurion-Enzo-SV244.aspx'  # NOQA
            }
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
    if not x or not y:
        print '404 #1'
        return HTTPError(404, reason="You used the wrong format, nerd.")
    if len(y) > 1 or len(x) > 1:
        print '400'
        return HTTPError(400, reason="This is not a valid square, nerd.")
    try:
        x = int(x)
        y = int(y)
    except TypeError:
        print '404 #2'
        return HTTPError(404, reason='You used the wrong format, nerd.')
    point = (x, y)
    if board[y][x] in [1, 0]:
        print '410'
        return HTTPError(
            410, reason='This square has already been attacked, nerd.'
        )
    hit = armada.check_hit(point)
    if str(hit) not in 'CBRSD':
        board[y][x] = hit
    else:
        board[y][x] = 1
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
    shot = request.forms.get('shot')
    if str(shot) not in 'CBRSD':
        enemy_board[y][x] = int(shot)
    else:
        enemy_board[y][x] = 2
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
def handle_400(*args):
    print '400'


@error(500)
def handle_500(*args):
    print '500'


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
    for ship in armada.ships:
        for location in armada.ships[ship].location:
            board[location[1]][location[0]] = ship
    print_armada()
    run(host='localhost', port=int(port), debug=True)

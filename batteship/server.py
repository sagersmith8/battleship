from bottle import route, run

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

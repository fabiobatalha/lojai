# coding: utf-8
import logging

logger = logging.getLogger(__name__)

def parse_create_matrix(x, y):
    """
    This method parses the args of the command I of the enunciation
    """
    x = int(x)
    y = int(y)

    if not x > 0 and not y > 0:
        raise ValueError('x and y must be positive intergers')

    return True

def parse_clean():
    """
    This method parses the args of the command C of the enunciation
    """

    return True

def parse_exit():
    """
    This method parses the args of the command X of the enunciation
    """

    return True

def parse_output_file(filename):
    """
    This method parses the args of the command S of the enunciation
    """

    if len(filename) == 0:
        raise ValueError('file names must be informed')

    return True

def parse_print_pixel(x, y, color):
    """
    This method parses the args of the command L of the enunciation

    Attributes:
    x -- integer
    y -- integer
    color -- any valid string or interger
    """
    x = int(x)
    y = int(y)

    if not x > 0 and not y > 0:
        raise ValueError('x and y must be positive intergers')

    return True

def parse_vertical_print(x, y1, y2, color):
    """
    This method parses the args of the command V of the enunciation

    Attributes:
    x -- integer (column index)
    y1 -- integer (vertical start point)
    y2 -- integer (vertical end point)
    color -- any valid string or interger
    """
    x = int(x)
    y1 = int(y1)
    y2 = int(y2)

    if not x >= 0 and not y1 >= 0 and not y2 >= 0:
        raise ValueError('x, y1 and y2 must be positive intergers')

    if not y2 >= y1:
        raise ValueError('y2 must be greather than y1')

    return True

def parse_horizontal_print(y, x1, x2, color):
    """
    This method parses the args of the command H of the enunciation

    Attributes:
    y -- integer (line index)
    x1 -- integer (horizontal start point)
    x2 -- integer (horizontal start point)
    color -- any valid string or interger
    """
    
    y = int(y)
    x1 = int(x1)
    x2 = int(x2)

    if not y > 0 and not x1 > 0 and not x2 > 0:
        raise ValueError('y, x1 and x2 must be positive intergers')

    if not x2 >= x1:
        raise ValueError('x2 must be greather than x1')

    return True

def parse_print_region(x, y, color):
    """
    This method parses the args of the command F of the enunciation

    Attributes:
    x -- integer
    y -- integer
    color -- any valid string or interger
    """
    x = int(x)
    y = int(y)

    if not x > 0 and not y > 0:
        raise ValueError('x and y must be positive intergers')

    return True

def parse_square_print(x1, y1, x2, y2, color):
    """
    This method parses the args of the command K of the enunciation

    Attributes:
    y -- integer (line index)
    x1 -- integer (horizontal start point)
    y1 -- integer (horizontal start point)
    x2 -- integer (horizontal start point)
    y2 -- integer (horizontal start point)
    color -- any valid string or interger
    """
    
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if not y1 > 0 and not y2 > 0 and not x1 > 0 and not x2 > 0:
        raise ValueError('y1, y2, x1 and x2 must be positive intergers')

    return True

ALLOWED_COMMANDS = {
    'I': parse_create_matrix,
    'C': parse_clean,
    'L': parse_print_pixel,
    'V': parse_vertical_print,
    'H': parse_horizontal_print,
    'K': parse_square_print,
    'S': parse_output_file,
    'X': parse_exit,
    'F': parse_print_region
}

def parse_command(args):
    """
    This method parse a command.

    Arguments:
    args -- [L, X, Y, C]
    """

    if len(args) == 0:
        msg = 'Skiping empty line'
        logger.warning(msg)
        raise ValueError(msg)

    command = ALLOWED_COMMANDS.get(args[0], None)
    params = args[1:]

    if not command:
        msg = 'Command not allowed %s' % str(args)
        logger.warning(msg)
        raise ValueError(msg)

    try:
        command(*params)
    except TypeError as e:
        msg = 'Invalid signature for command %s' % str(args)
        logger.warning(msg)
        raise e

    return (args[0], params)

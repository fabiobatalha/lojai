# coding: utf-8
import argparse
import logging
import logging.config

from paint.canvas import Canvas

logger = logging.getLogger(__name__)

LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'NOTSET',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        'paint': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}

logging.config.dictConfig(LOGGING)


def parse_file(filename):
    """
    This method read the input file with the commands and parse each command.
    The error are thrown to the stdout.
    """
    try:
        fname = open(filename, 'r')
    except:
        logger.error('File do no exists %s' % filename)

    with fname as f:
        for line in f:
            if line.strip()[0] == "#":
                continue

            command = line.strip().upper().split(' ')

            yield (command[0], command[1:])


def run(filename):

    canvas = Canvas()

    mapping = {
        'I': canvas.build_canvas,
        'L': canvas.print_pixel,
        'S': canvas.write_file,
        'V': canvas.print_vertical,
        'H': canvas.print_horizontal,
        'F': canvas.print_region,
        'K': canvas.print_square,
        'X': 'exit'
    }

    iteration = 0
    for command, params in parse_file(filename):
        iteration += 1
        print('round (%d): %s %s' % (iteration, command, str(params)))
        if command == 'X':
            exit()
        try:
            mapping[command](*params)
        except KeyError:
            logger.warning('Unkow command %s, skipping command.' % command)

        print(canvas.picture)


def main():

    parser = argparse.ArgumentParser(
        description='Paint Canvas according to a file with commands.'
    )

    parser.add_argument(
        '--input_file',
        '-i',
        required=True,
        help='filename with commands'
    )

    args = parser.parse_args()

    run(args.input_file)

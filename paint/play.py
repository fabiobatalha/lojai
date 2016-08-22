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
        'masterchess': {
            'handlers': ['console'],
            'level': 'DEBUG'
        }
    }
}

logging.config.dictConfig(LOGGING)

ALLOWED_COMMANDS = ['I', 'C', 'L', 'V', 'H', 'K', 'F', 'S', 'X']


def read_file(filename):

    try:
        fname = open(filename, 'r')
    except:
        logger.error('File do no exists %s' % filename)

    with fname as f:
        for line in f:
            command = line.strip().upper().split(' ')
            if command[0] not in ALLOWED_COMMANDS:
                continue

            yield command


def run(filename):

    for command in read_file(filename):
        print(command)


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
